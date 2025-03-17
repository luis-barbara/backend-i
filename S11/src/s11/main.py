from fastapi import FastAPI, HTTPException
import logging
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

items = {}

@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to the FastAPI API!"}

@app.post("/items/")
async def create_item(item: Item):
    logger.info(f"Item received: {item}")
    item_id = len(items) + 1
    items[item_id] = item
    return {"item_id": item_id, "item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f"Updating item: {item_id} with data {item}")
    if item_id not in items:
        logger.error(f"Item with id {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f"Attempting to delete item: {item_id}")
    if item_id not in items:
        logger.error(f"Item with id {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items.pop(item_id)
    return {"message": f"Item {item_id} deleted", "deleted_item": deleted_item}


# Run the application using Uvicorn with:
# poetry run uvicorn main:app --reload