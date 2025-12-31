import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from aiogram.types import Update
from contextlib import asynccontextmanager

from bot import bot, dp, WEBHOOK_PATH, set_webhook, delete_webhook

from shared.logger.logger import logger


@asynccontextmanager
async def lifespan(app : FastAPI):
    try:
        await set_webhook()
    except:
        pass
    logger.info("Start telegram_bot service")
    yield
    await delete_webhook()
    await bot.session.close()
    logger.info("Shutdown telegram_bot service")
    


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health():
    return JSONResponse(
        content={"detail" : "Telegram bot service start succses"}, 
        status_code=status.HTTP_200_OK
        )


@app.post(WEBHOOK_PATH)
async def bot_webhook(request : Request, update: dict):
    """Обработка всех событий бота"""
    try:
        logger.info("ОБрабатываю запрос бот...")
        telegram_update = Update(**update)
        await dp.feed_webhook_update(bot, telegram_update)
        return {"status": "ok"}
    except Exception as e:
        return JSONResponse(content={"details" : str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


if __name__ == "__main__":
    uvicorn.run("telegram_bot.main:app", port=8003, host="0.0.0.0", reload=True)