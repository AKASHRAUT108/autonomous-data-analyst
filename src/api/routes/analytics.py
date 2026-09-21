from pathlib import Path

import pandas as pd
from fastapi import APIRouter, HTTPException
from src.api.schemas import AnalyticsStatusResponse

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[3]


# ---------------------------------------------------------
# 9.10 — Business Summary
# ---------------------------------------------------------

@router.get("/summary")
async def analytics_summary():

    file_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "business_overview.csv"
    )

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Business overview data not found."
        )

    df = pd.read_csv(file_path)

    return {
        "status": "success",
        "rows": len(df),
        "columns": df.columns.tolist(),
        "data": df.to_dict(orient="records")
    }


# ---------------------------------------------------------
# 9.11 — Customer Segments
# ---------------------------------------------------------

@router.get("/segments")
async def customer_segments():

    file_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "customer_segment_summary.csv"
    )

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Customer segment data not found."
        )

    df = pd.read_csv(file_path)

    return {
        "status": "success",
        "rows": len(df),
        "columns": df.columns.tolist(),
        "segments": df.to_dict(orient="records")
    }


# ---------------------------------------------------------
# 9.12 — Product Performance
# ---------------------------------------------------------

@router.get("/products")
async def product_performance():

    file_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "business_product_performance.csv"
    )

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Product performance data not found."
        )

    df = pd.read_csv(file_path)

    return {
        "status": "success",
        "rows": len(df),
        "columns": df.columns.tolist(),
        "products": df.to_dict(orient="records")
    }


# ---------------------------------------------------------
# 9.13 — Country Performance
# ---------------------------------------------------------

@router.get("/countries")
async def country_performance():

    file_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "business_country_performance.csv"
    )

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Country performance data not found."
        )

    df = pd.read_csv(file_path)

    return {
        "status": "success",
        "rows": len(df),
        "columns": df.columns.tolist(),
        "countries": df.to_dict(orient="records")
    }


# ---------------------------------------------------------
# 9.14 — ML Customer Opportunities
# ---------------------------------------------------------

@router.get("/ml-opportunities")
async def ml_opportunities():

    file_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "customer_opportunity_summary.csv"
    )

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="ML opportunity data not found."
        )

    df = pd.read_csv(file_path)

    return {
        "status": "success",
        "rows": len(df),
        "columns": df.columns.tolist(),
        "opportunities": df.to_dict(orient="records")
    }


# ---------------------------------------------------------
# 9.15 — Business Recommendations
# ---------------------------------------------------------

@router.get("/recommendations")
async def business_recommendations():

    file_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "business_recommendations.csv"
    )

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Business recommendations data not found."
        )

    df = pd.read_csv(file_path)

    return {
        "status": "success",
        "rows": len(df),
        "columns": df.columns.tolist(),
        "recommendations": df.to_dict(orient="records")
    }


# ---------------------------------------------------------
# 9.16 — Business Insights
# ---------------------------------------------------------

@router.get("/insights")
async def business_insights():

    file_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "business_insights.csv"
    )

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Business insights data not found."
        )

    df = pd.read_csv(file_path)

    return {
        "status": "success",
        "rows": len(df),
        "columns": df.columns.tolist(),
        "insights": df.to_dict(orient="records")
    }


# ---------------------------------------------------------
# 9.17 — High-Value Customers
# ---------------------------------------------------------

@router.get("/high-value-customers")
async def high_value_customers():

    file_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "customer_rfm_segments.csv"
    )

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Customer RFM data not found."
        )

    df = pd.read_csv(file_path)

    high_value = (
        df.sort_values(
            by="Monetary",
            ascending=False
        )
        .head(20)
    )

    return {
        "status": "success",
        "count": len(high_value),
        "customers": high_value.to_dict(orient="records")
    }


# ---------------------------------------------------------
# 9.18 — Dataset Status
# ---------------------------------------------------------

@router.get("/status")
async def analytics_status():

    files = {
        "business_overview":
            PROJECT_ROOT / "data" / "processed" / "business_overview.csv",

        "customer_segments":
            PROJECT_ROOT / "data" / "processed" / "customer_segment_summary.csv",

        "product_performance":
            PROJECT_ROOT / "data" / "processed" / "business_product_performance.csv",

        "country_performance":
            PROJECT_ROOT / "data" / "processed" / "business_country_performance.csv",

        "ml_opportunities":
            PROJECT_ROOT / "data" / "processed" / "customer_opportunity_summary.csv",

        "recommendations":
            PROJECT_ROOT / "data" / "processed" / "business_recommendations.csv",

        "insights":
            PROJECT_ROOT / "data" / "processed" / "business_insights.csv",

        "rfm_segments":
            PROJECT_ROOT / "data" / "processed" / "customer_rfm_segments.csv"
    }

    status = {
        name: path.exists()
        for name, path in files.items()
    }

    available = sum(status.values())
    total = len(status)

    return {
        "status": "success",
        "available_files": available,
        "total_files": total,
        "datasets": status
    }@router.get(
    "/status",
    response_model=AnalyticsStatusResponse
)
async def analytics_status():

    files = {
        "business_overview":
            PROJECT_ROOT / "data" / "processed" / "business_overview.csv",

        "customer_segments":
            PROJECT_ROOT / "data" / "processed" / "customer_segment_summary.csv",

        "product_performance":
            PROJECT_ROOT / "data" / "processed" / "business_product_performance.csv",

        "country_performance":
            PROJECT_ROOT / "data" / "processed" / "business_country_performance.csv",

        "ml_opportunities":
            PROJECT_ROOT / "data" / "processed" / "customer_opportunity_summary.csv",

        "recommendations":
            PROJECT_ROOT / "data" / "processed" / "business_recommendations.csv",

        "insights":
            PROJECT_ROOT / "data" / "processed" / "business_insights.csv",

        "rfm_segments":
            PROJECT_ROOT / "data" / "processed" / "customer_rfm_segments.csv"
    }

    status = {
        name: path.exists()
        for name, path in files.items()
    }

    available = sum(status.values())
    total = len(status)

    return {
        "status": "success",
        "available_files": available,
        "total_files": total,
        "datasets": status
    }