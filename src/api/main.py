import traceback
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
    }

# 10.12 - Temporary detailed error handler

import traceback

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):

    print("\n" + "=" * 70)
    print("FASTAPI ERROR")
    print("=" * 70)

    traceback.print_exc()

    print("=" * 70 + "\n")

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": str(exc),
            "path": request.url.path
        }
    )
