from fastapi import FastAPI

from app.api.auth import router as auth_router

app = FastAPI(
    title="Airport Management System",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Airport Management System Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }