from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class DatasetStatus(BaseModel):
    business_overview: bool
    customer_segments: bool
    product_performance: bool
    country_performance: bool
    ml_opportunities: bool
    recommendations: bool
    insights: bool
    rfm_segments: bool


class AnalyticsStatusResponse(BaseModel):
    status: str
    available_files: int
    total_files: int
    datasets: DatasetStatus