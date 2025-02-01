from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import connect_to_mongo, close_mongo_connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI backend"}

from app.routers import items
app.include_router(items.router, prefix="/api")