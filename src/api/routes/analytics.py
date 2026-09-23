from pathlib import Path
import math
import pandas as pd
from fastapi import APIRouter, HTTPException
from src.api.schemas import AnalyticsStatusResponse
from src.analysis.ai_analyst import classify_question
from src.analysis.answer_engine import answer_question
from pathlib import Path


PROCESSED_DIR = Path("data/processed")

def clean_for_json(data):
    if isinstance(data, dict):
        return {key: clean_for_json(value) for key, value in data.items()}

    if isinstance(data, list):
        return [clean_for_json(value) for value in data]

    if isinstance(data, float):
        if math.isnan(data) or math.isinf(data):
            return None

    return data


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


# -# ---------------------------------------------------------
# 10.12 — Product Performance Endpoint
# ---------------------------------------------------------

@router.get("/products")
async def product_performance():

    file_path = PROCESSED_DIR / "business_product_performance.csv"

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Product performance data not found."
        )

    try:
        df = pd.read_csv(file_path)

        # Replace infinite values with missing values
        df = df.replace([float("inf"), float("-inf")], pd.NA)

        # Convert missing values to JSON-safe None
        df = df.astype(object).where(pd.notna(df), None)

        products = df.to_dict(orient="records")

        result = {
            "status": "success",
            "rows": len(products),
            "columns": df.columns.tolist(),
            "products": products
        }

        return clean_for_json(result)

    except Exception as e:
        import traceback

        print("\n===== PRODUCT API ERROR =====")
        print(str(e))
        traceback.print_exc()
        print("=============================\n")

        return {
            "status": "error",
            "message": str(e),
            "path": "/analytics/products"
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
@router.get(
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

# ---------------------------------------------------------
# 11.1 — AI Analyst
# ---------------------------------------------------------

# ---------------------------------------------------------
# 11.7 — AI Analyst API
# ---------------------------------------------------------

@router.get("/ask")
async def ask_analyst(question: str):

    if not question.strip():
        return {
            "status": "error",
            "question": question,
            "message": "Please provide a question."
        }

    question_type = classify_question(question)

    answer = answer_question(
        question,
        question_type
    )

    return {
        "status": "success",
        "question": question,
        "question_type": question_type,
        "answer": answer
    }
    # -----------------------------------------
    # Revenue questions
    # -----------------------------------------

    if "total revenue" in question_lower:

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
            "question": question,
            "answer": f"Total revenue generated was approximately {df['total_revenue'].iloc[0]:,.2f}."
        }

    # -----------------------------------------
    # Customer questions
    # -----------------------------------------

    if "customer" in question_lower and "count" in question_lower:

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
            "question": question,
            "answer": f"The analysis contains approximately {int(df['total_customers'].iloc[0]):,} customers."
        }

    # -----------------------------------------
    # Product questions
    # -----------------------------------------

    if "top product" in question_lower:

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

        revenue_column = None

        for column in df.columns:
            if column.lower() in ["revenue", "total_revenue"]:
                revenue_column = column
                break

        if revenue_column is None:
            return {
                "status": "error",
                "question": question,
                "answer": "Revenue information is not available in the product dataset."
            }

        top_product = df.sort_values(
            revenue_column,
            ascending=False
        ).iloc[0]

        return {
            "status": "success",
            "question": question,
            "answer": (
                f"The top-performing product generated "
                f"{top_product[revenue_column]:,.2f} in revenue."
            )
        }

    # -----------------------------------------
    # Segment questions
    # -----------------------------------------

    if "segment" in question_lower:

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

        if "avg_monetary" in df.columns:

            top_segment = df.sort_values(
                "avg_monetary",
                ascending=False
            ).iloc[0]

            return {
                "status": "success",
                "question": question,
                "answer": (
                    f"The segment with the highest average customer value "
                    f"is {top_segment['segment']}."
                )
            }

    # -----------------------------------------
    # Default response
    # -----------------------------------------

    return {
        "status": "success",
        "question": question,
        "answer": (
            "I could not identify a specific analytical operation for this question yet. "
            "Try asking about total revenue, customer count, top product, or customer segments."
        )
    }