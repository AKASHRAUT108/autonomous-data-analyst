from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


def get_business_metric(metric_name: str):
    """
    Get a business metric from business_overview.csv.

    The CSV structure is:

    Metric | Value
    """

    file_path = PROCESSED_DIR / "business_overview.csv"

    df = pd.read_csv(file_path)

    row = df[
        df["Metric"].astype(str).str.strip().str.lower()
        == metric_name.strip().lower()
    ]

    if row.empty:
        return None

    return row["Value"].iloc[0]


def answer_question(question: str, question_type: str) -> str:

    # --------------------------------
    # REVENUE
    # --------------------------------
    if question_type == "revenue":

        revenue = get_business_metric("Total Revenue")

        if revenue is None:
            return "Total revenue information is not available."

        return f"Total revenue generated was {float(revenue):,.2f}."


    # --------------------------------
    # CUSTOMER COUNT
    # --------------------------------
    if question_type == "customer_count":

        customers = get_business_metric("Total Customers")

        if customers is None:
            return "Customer count information is not available."

        return f"The analysis contains {int(float(customers)):,} customers."


    # --------------------------------
    # ORDERS
    # --------------------------------
    if question_type == "orders":

        orders = get_business_metric("Total Orders")

        if orders is None:
            return "Order information is not available."

        return f"The business recorded {int(float(orders)):,} orders."


    # --------------------------------
    # TOP PRODUCT
    if question_type == "top_product":
        file_path = PROCESSED_DIR / "business_product_performance.csv"

        if not file_path.exists():
            return "Product performance data is not available."

        df = pd.read_csv(file_path)

        revenue_column = None
        product_column = None

        for column in df.columns:
            column_lower = column.lower().strip()

            if column_lower in [
                "revenue",
                "total_revenue",
                "monetary",
                "total_sales",
                "sales"
            ]:
                revenue_column = column

            if column_lower in [
                "product",
                "description",
                "product_name",
                "stockcode",
                "stock_code"
            ]:
                product_column = column

        if revenue_column is None:
            return "Product revenue information is not available."

        top_product = df.sort_values(
            revenue_column,
            ascending=False
        ).iloc[0]

        revenue = float(top_product[revenue_column])

        if product_column is not None:
            product_name = str(top_product[product_column])

            return (
                f"The top product was "
                f"'{product_name}', "
                f"generating {revenue:,.2f} in revenue."
            )

        return (
            f"The top product generated "
            f"{revenue:,.2f} in revenue."
        )


    # --------------------------------
    # CUSTOMER SEGMENT
    if question_type == "segment":
        file_path = PROCESSED_DIR / "customer_segment_summary.csv"

        if not file_path.exists():
            return "Customer segment data is not available."

        df = pd.read_csv(file_path)

        # Normalize column names for matching
        column_map = {
            column.strip().lower().replace(" ", "_"): column
            for column in df.columns
        }

        # Find segment column
        segment_column = None

        for key, original_column in column_map.items():
            if (
                key == "segment"
                or "segment" in key
            ):
                segment_column = original_column
                break

        # Find customer-value column
        value_column = None

        preferred_value_names = [
            "avg_monetary",
            "average_monetary",
            "avg_customer_value",
            "average_customer_value",
            "monetary",
            "avg_revenue",
            "average_revenue",
            "revenue"
        ]

        for name in preferred_value_names:
            if name in column_map:
                value_column = column_map[name]
                break

        if segment_column is None:
            return (
                "Customer segment name information "
                "is not available."
            )

        if value_column is None:
            return (
                "Customer segment value information "
                "is not available."
            )

        # Make sure the value column is numeric
        df[value_column] = pd.to_numeric(
            df[value_column],
            errors="coerce"
        )

        df = df.dropna(subset=[value_column])

        if df.empty:
            return "Customer segment value data is not available."

        top_segment = df.sort_values(
            value_column,
            ascending=False
        ).iloc[0]

        segment_name = str(
            top_segment[segment_column]
        )

        average_value = float(
            top_segment[value_column]
        )

        return (
            f"The customer segment with the highest "
            f"average customer value is "
            f"'{segment_name}', "
            f"with an average value of "
            f"{average_value:,.2f}."
        )
    # --------------------------------
    # COUNTRY
    # --------------------------------
    if question_type == "country":

        file_path = (
            PROCESSED_DIR /
            "business_country_performance.csv"
        )

        if not file_path.exists():
            return "Country performance data is not available."

        df = pd.read_csv(file_path)

        revenue_column = None
        country_column = None

        for column in df.columns:

            column_lower = column.lower()

            if column_lower in [
                "revenue",
                "total_revenue",
                "sales",
                "total_sales"
            ]:
                revenue_column = column

            if column_lower in [
                "country",
                "countries"
            ]:
                country_column = column

        if revenue_column is None:
            return "Country revenue information is not available."

        if country_column is None:
            return "Country name information is not available."

        top_country = df.sort_values(
            revenue_column,
            ascending=False
        ).iloc[0]

        return (
            f"The country with the highest revenue is "
            f"{top_country[country_column]}, "
            f"with revenue of "
            f"{float(top_country[revenue_column]):,.2f}."
        )


    # --------------------------------
    # UNKNOWN QUESTION
    # --------------------------------
    return (
        "I could not identify an analytical "
        "operation for this question yet."
    )