from fastapi import APIRouter, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorCollection
from ..database import get_database
from ..models.item import Item, ItemCreate

router = APIRouter()

@router.get("/items", response_model=list[Item])
async def get_items():
    try:
        db = get_database()
        collection: AsyncIOMotorCollection = db["items"]
        items = await collection.find().to_list(1000)
        return [Item(**item) for item in items]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    try:
        db = get_database()
        collection: AsyncIOMotorCollection = db["items"]
        result = await collection.insert_one(item.dict())
        new_item = await collection.find_one({"_id": result.inserted_id})
        return Item(**new_item)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )