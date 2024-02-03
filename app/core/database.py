from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url="sqlite://:memory:",  # Replace with your PostgreSQL URL
        modules={'models': ['app.api.models']}
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()
