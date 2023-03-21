# from sqlalchemy import create_engine, orm
from sqlalchemy.ext.asyncio import create_async_engine


async def create_database(url: str) -> None:
    engine = create_async_engine(
        url,
        pool_pre_ping=True,
        future=True,
    )
    await engine.dispose()
