from fastapi import APIRouter, Depends, HTTPException
from app.api import crud
from app.core.security import get_current_user
from typing import List

router = APIRouter()

@router.post("/portfolio", response_model=dict)
async def create_portfolio_item(name: str, description: str, current_user: dict = Depends(get_current_user)):
    return await crud.create_portfolio_item(name, description)

@router.get("/portfolio", response_model=List[dict])
async def read_portfolio_items():
    return await crud.get_portfolio_items()

@router.get("/portfolio/{item_id}", response_model=dict)
async def read_portfolio_item(item_id: int):
    item = await crud.get_portfolio_item(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/portfolio/{item_id}", response_model=dict)
async def update_portfolio_item(item_id: int, name: str, description: str):
    item = await crud.update_portfolio_item(item_id, name, description)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/portfolio/{item_id}", response_model=dict)
async def delete_portfolio_item(item_id: int):
    item = await crud.delete_portfolio_item(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")
