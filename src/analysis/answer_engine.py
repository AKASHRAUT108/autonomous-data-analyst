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
    if question_type == "segment":
        file_path = PROCESSED_DIR / "customer_rfm_segments.csv"

        if not file_path.exists():
            return "Customer RFM segment data is not available."

        df = pd.read_csv(file_path)

        # Find the actual segment column
        segment_column = None
        monetary_column = None

        for column in df.columns:
            column_lower = str(column).strip().lower()

            if column_lower == "segment":
                segment_column = column

            if column_lower == "monetary":
                monetary_column = column

        if segment_column is None:
            return "Customer segment information is not available."

        if monetary_column is None:
            return "Customer monetary value information is not available."

        # Convert monetary values to numeric
        df[monetary_column] = pd.to_numeric(
            df[monetary_column],
            errors="coerce"
        )

        df = df.dropna(
            subset=[segment_column, monetary_column]
        )

        if df.empty:
            return "Customer segment value data is not available."

        # Calculate average customer value for each segment
        segment_values = (
            df.groupby(segment_column)[monetary_column]
            .mean()
            .reset_index()
        )

        # Find segment with highest average customer value
        top_segment = segment_values.sort_values(
            monetary_column,
            ascending=False
        ).iloc[0]

        segment_name = str(
            top_segment[segment_column]
        )

        average_value = float(
            top_segment[monetary_column]
        )

        return (
            f"The customer segment with the highest "
            f"average customer value is "
            f"'{segment_name}', "
            f"with an average value of "
            f"{average_value:,.2f}."
        )
    # --------------------------------
    # UNKNOWN QUESTION
    # --------------------------------
    return (
        "I could not identify an analytical "
        "operation for this question yet."
    )