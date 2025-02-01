
import os
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from contextlib import asynccontextmanager

DB_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DB", "mydatabase")

client = None

@asynccontextmanager
async def connect_to_mongo(app: FastAPI):
    global client
    client = AsyncIOMotorClient(DB_URL)
    await client.server_info()
    yield
    await close_mongo_connection()

async def close_mongo_connection():
    if client:
        client.close()

def get_database():
    return client[DB_NAME]