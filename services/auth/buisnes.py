from typing import Optional, Callable, cast
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from db.repository import AUoW
from schema import ServiceUserRegisterRequest, ServiceUserRegisterWithTelegramRequest
from serializer import UserModelSerializer
from utils.sms import generate_session_pair
from utils.jwt import create_access_token, create_refresh_token

from shared.logger.logger import logger
from shared.service.base import BaseService

class AuthService(BaseService[AUoW]):
    def __init__(
            self, 
            uow_factory : Optional[Callable[[], type[AUoW]]] = None, 
            user_serializer : Optional[Callable[[], SQLAlchemyAutoSchema]] = None 
            ):
        super().__init__(uow_factory)
        self._user_serializer = user_serializer() or UserModelSerializer()

    @BaseService.transactional()
    async def register(self, data : ServiceUserRegisterRequest):
        logger.debug(f"Попытка login {data.phone_number} - {data.password}")
        
    
    @BaseService.transactional()
    async def register_with_telegram(self, data : ServiceUserRegisterWithTelegramRequest):
        logger.debug(f"Попытка login {data.telegram_id}")
        

            
    async def login(self):
        pass

    async def authorized(self):
        pass

    async def refresh(self):
        pass