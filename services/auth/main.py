import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager


from shared.logger.logger import logger
from api import main_router

@asynccontextmanager
async def lifespan(app : FastAPI):
    logger.info("Start auth service")
    yield
    logger.info("Shutdown auth service")


app = FastAPI(lifespan=lifespan)
app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, host="0.0.0.0", reload=True)