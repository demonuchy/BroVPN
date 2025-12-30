from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine, async_sessionmaker
from contextlib import asynccontextmanager
from shared.config import config


engine = create_async_engine(
    url=config.AsyncDataBaseUrl,
    echo = False
    )

session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False, 
    class_=AsyncSession
    )


async def get_session():
    async with session_factory() as session:
        yield session
