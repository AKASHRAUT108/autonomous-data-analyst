import pandas as pd 
def calculate_sales_matrics(df:pd.dataFrame)->dict:
    """Calculate core business sales metrics."""
    metrics={
        "total_revenue":float(df["revenue"].sum()),
        "total_transactions":int(df["invoice"].nunique()),
        "total_products":int(df["stock_code"].nunique()),
        "total_customers":int(df["customer_id"].nunique()),
        "total_countries":int(df["country"].nunique()),
        "average_order_value":float(
            df.groupby("invoice")["revenue"].sum().mean()
        )
    }

    return metrics