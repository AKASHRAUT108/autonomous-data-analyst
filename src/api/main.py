from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.analytics import router as analytics_router
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.api.routes.upload import router as upload_router

app = FastAPI(
    title="Autonomous Data Analyst API",
    description="AI-powered Business Intelligence and Data Analytics API",
    version="1.0.0"
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(analytics_router)
app.include_router(upload_router)

@app.get("/")
async def root():
    return {
        "message": "Autonomous Data Analyst API is running",
        "status": "success",
        "version": "1.0.0"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "An unexpected error occurred.",
            "path": str(request.url.path)
        }
    )