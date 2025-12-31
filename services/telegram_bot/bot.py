import os
import sys
import asyncio
import logging
import json
from typing import Any, Callable, Dict, Awaitable
from aiogram import Bot, Dispatcher, types, F, BaseMiddleware

from shared.config import config
from shared.logger.logger import logger



WEBHOOK_PATH = f"/bot/{config.TOKEN_BOT}"
WEBHOOK_URL = f"{config.WEBHOOK_TUNNEL_URL}{WEBHOOK_PATH}"


bot = Bot(token=config.TOKEN_BOT)
dp = Dispatcher()


async def set_webhook():
    """Установка вебхука"""
    await bot.set_webhook(
        url=WEBHOOK_URL,
        secret_token=config.WEBHOOK_SECRET_KEY,
        drop_pending_updates=True,
        allowed_updates=["message", "callback_query", "web_app_data"]
    )
    logger.info(f"Вебхук установлен: {WEBHOOK_URL}")


async def delete_webhook():
    """Удаление вебхука"""
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Вебхук удален")