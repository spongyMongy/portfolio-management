from tortoise.query_utils import Q
from app.api.models import PortfolioItem

async def create_portfolio_item(name: str, description: str):
    return await PortfolioItem.create(name=name, description=description)

async def get_portfolio_items():
    return await PortfolioItem.all()

async def get_portfolio_item(item_id: int):
    return await PortfolioItem.get_or_none(id=item_id)

async def update_portfolio_item(item_id: int, name: str, description: str):
    return await PortfolioItem.filter(id=item_id).update(name=name, description=description)

async def delete_portfolio_item(item_id: int):
    return await PortfolioItem.filter(id=item_id).delete()
