import asyncio
from fastapi import WebSocket
from app.api import crud

async def portfolio_item_added(websocket: WebSocket):
    while True:
        item = await websocket.receive_text()
        await crud.create_portfolio_item(name=item, description="Real-time update")
        await asyncio.sleep(1)
