import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from shared.logger.logger import logger

@asynccontextmanager
async def lifespan(app : FastAPI):
    logger.info("Start telegram_bot service")
    yield
    logger.info("Shutdown telegram_bot service")



app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run("telegram_bot.main:app", port=8001, host="0.0.0.0", reload=True)