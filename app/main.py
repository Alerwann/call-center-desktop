# app/main.py
import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app.config.settings import settings
from app.core.database import connect_database
from app.api.v1.router import api_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    """
        function faisant la connection à la base de donnée
        note: fonction async
    """
    await connect_database()
    print(f"🚀 Server running on port {settings.port}")
    yield
    print("🛑 Shutting down...")

def create_app() -> FastAPI:
    """Creation  du cors pour connexion server"""
    app = FastAPI(title="HR System API", version="1.0.0", lifespan=lifespan)

    # CORS (équivalent de ton app.use(cors))
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
        allow_headers=["*"],
    )
    app.include_router(api_router)
    return app


app = create_app()
