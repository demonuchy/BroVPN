import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from api import main_router
from db.context import db_health_check

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

@app.get("/db/health")
async def db_health():
    try:
        result = await db_health_check()
        if result == 1:
            return  JSONResponse(
            content={"detail" : "Auth service the connection to the database is established"}, 
            status_code=status.HTTP_200_OK
            )
        logger.warn(f"Ошибка подключения к бд : {result}")
        return JSONResponse(
            content={"detail" : "Auth service the connection to the database is failed !"}, 
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE
            )
    except Exception as e:
        logger.warn(f"Ошибка подключения к бд {str(e)}")
        return JSONResponse(
            content={"detail" : "Auth service the connection to the database ian unforeseen event!"}, 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, host="0.0.0.0", reload=True)