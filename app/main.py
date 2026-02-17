from fastapi import FastAPI
from app.routers.health import router as health_router
app = FastAPI(title="LoL Stats Service API", version="0.0.1")
app.include_router(health_router)
