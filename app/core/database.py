# app/core/database.py
from motor.motor_asyncio import AsyncIOMotorClient
import sys
import ssl
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.settings import settings

# Variable globale pour la connexion
database = None
client = None


async def connect_database():
    """Connexion à MongoDB avec Motor (async)"""
    global database, client

    try:
        # Motor pour FastAPI (async)
        client = AsyncIOMotorClient(
            settings.MONGODB_URI, tlsAllowInvalidCertificates=True
        )

        # Test de connexion
        await client.admin.command("ping")

        # Sélection de la DB (extrait du URI ou nom fixe)
        database = client.get_default_database()  # ou client["hr_system"]

        print(f"✅ MongoDB connectée: {settings.MONGODB_URI}")

    except Exception as e:
        print(f"❌ Erreur connexion MongoDB: {e}")
        raise e


async def get_database():
    """Getter pour récupérer la DB dans les routes"""
    return database
