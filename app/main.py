from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from app.api.routes import router as portfolio_router
from app.api.auth import router as auth_router
from app.api.websocket import portfolio_item_added
from app.core.config import DATABASE_URL, SECRET_KEY, ALGORITHM
from app.core.database import init_db, close_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(portfolio_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["app.api.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.websocket("/ws/portfolio")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await portfolio_item_added(websocket)

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.on_event("shutdown")
async def shutdown_event():
    await close_db()
