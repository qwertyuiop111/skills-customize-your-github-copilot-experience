"""
FastAPI REST API Starter Code
Build a REST API for managing items (e.g., to-do tasks, books, students)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(
    title="Item Management API",
    description="A simple REST API for managing items",
    version="1.0.0"
)

# Pydantic model for request/response validation
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    completed: bool = False

# Mock database - replace with real database later
items_db: List[Item] = [
    Item(id=1, name="Learn FastAPI", description="Complete FastAPI tutorial", completed=False),
    Item(id=2, name="Build REST API", description="Create a simple REST API", completed=False),
]

# TODO: Implement the following endpoints:

# 1. GET /items - Retrieve all items
# Expected response: List of all items
@app.get("/items", response_model=List[Item])
def get_all_items():
    """Retrieve all items from the database"""
    # TODO: Implementation here
    pass

# 2. GET /items/{item_id} - Retrieve a specific item by ID
# Expected response: Single item or 404 error if not found
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """Retrieve a specific item by ID"""
    # TODO: Implementation here
    pass

# 3. POST /items - Create a new item
# Expected response: Created item with assigned ID
@app.post("/items", response_model=Item)
def create_item(item: Item):
    """Create a new item"""
    # TODO: Implementation here
    pass

# 4. PUT /items/{item_id} - Update an existing item
# Expected response: Updated item or 404 error if not found
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    """Update an existing item"""
    # TODO: Implementation here
    pass

# 5. DELETE /items/{item_id} - Delete an item
# Expected response: Confirmation or 404 error if not found
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item"""
    # TODO: Implementation here
    pass

# Run the server with: uvicorn starter-code:app --reload
