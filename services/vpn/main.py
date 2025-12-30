import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from shared.logger.logger import logger

@asynccontextmanager
async def lifespan(app : FastAPI):
    logger.info("Start vpn service")
    yield
    logger.info("Shutdown vpn service")


app = FastAPI(lifespan=lifespan)

@app.get("/health")
async def health():
    return JSONResponse(
        content={"detail" : "Vpn service start succses"}, 
        status_code=status.HTTP_200_OK
        )

if __name__ == "__main__":
    uvicorn.run("main:app", port=8002, host="0.0.0.0", reload=True)