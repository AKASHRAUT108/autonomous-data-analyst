import pandas as pd


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize raw dataset column names."""

    df = df.copy()

    column_mapping = {
        "Invoice": "invoice",
        "StockCode": "stock_code",
        "Description": "description",
        "Quantity": "quantity",
        "InvoiceDate": "invoice_date",
        "Price": "price",
        "Customer ID": "customer_id",
        "Country": "country",
    }

    return df.rename(columns=column_mapping)


def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """Convert columns to appropriate data types."""

    df = df.copy()

    df["quantity"] = pd.to_numeric(
        df["quantity"],
        errors="coerce"
    )

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    df["invoice_date"] = pd.to_datetime(
        df["invoice_date"],
        errors="coerce"
    )

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove exact duplicate transaction records."""

    df = df.copy()

    return df.drop_duplicates()


def add_cancellation_flag(df: pd.DataFrame) -> pd.DataFrame:
    """Identify cancelled invoices."""

    df = df.copy()

    df["is_cancelled"] = (
        df["invoice"]
        .astype(str)
        .str.startswith("C")
    )

    return df


def add_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate transaction revenue."""

    df = df.copy()

    df["revenue"] = df["quantity"] * df["price"]

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Run the complete data cleaning pipeline."""

    df = standardize_columns(df)
    df = convert_data_types(df)
    df = remove_duplicates(df)
    df = add_cancellation_flag(df)
    df = add_revenue(df)

    return df

def validate_data(df: pd.DataFrame) -> dict:
    """Validate the cleaned dataset and return a quality report."""

    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "invalid_dates": int(df["invoice_date"].isnull().sum()),
        "invalid_quantities": int(df["quantity"].isnull().sum()),
        "invalid_prices": int(df["price"].isnull().sum()),
        "negative_quantities": int((df["quantity"] < 0).sum()),
        "negative_prices": int((df["price"] < 0).sum()),
        "cancelled_transactions": int(df["is_cancelled"].sum()),
    }

    return report