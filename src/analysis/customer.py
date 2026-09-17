import pandas as pd


def calculate_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate Recency, Frequency and Monetary values
    for each customer.
    """

    data = df.copy()

    # Keep rows with a known customer
    data = data.dropna(subset=["customer_id"])

    # Remove cancelled transactions
    if "is_cancelled" in data.columns:
        data = data[data["is_cancelled"] == False]

    # Keep valid revenue
    data = data[data["revenue"] > 0]

    # Reference date = one day after the latest transaction
    reference_date = data["invoice_date"].max() + pd.Timedelta(days=1)

    rfm = (
        data.groupby("customer_id")
        .agg(
            Recency=(
                "invoice_date",
                lambda x: (reference_date - x.max()).days
            ),
            Frequency=("invoice", "nunique"),
            Monetary=("revenue", "sum"),
        )
        .reset_index()
    )

    return rfm