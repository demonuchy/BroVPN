import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from .api import main_router

from shared.logger.logger import logger

@asynccontextmanager
async def lifespan(app : FastAPI):
    logger.info("Start auth service")
    yield
    logger.info("Shutdown auth service")


app = FastAPI(lifespan=lifespan)

@app.get("/health")
async def health():
    return JSONResponse(
        content={"detail" : "Auth service start succses"}, 
        status_code=status.HTTP_200_OK
        )

app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, host="0.0.0.0", reload=True)