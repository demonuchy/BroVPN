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
from shared.database.base import BaseUnitOfWork
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
        user = await self.uow.user_repository.get_by_field("phone_number", data.phone_number)
        if user:
            logger.warn("Пользователь уже существует")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail="Пользователь уже существует"
                )
        hash_password = data.password
        user = await self.uow.user_repository.create(...)
        _, access_token = create_access_token(user.id)
        jti, refresh_token = create_refresh_token(user.id)
        session = await self.uow.session_repository.create(...)
        logger.debug("Пользователь создан")
        return ...  
    
    @BaseService.transactional()
    async def register_with_telegram(self, data : ServiceUserRegisterWithTelegramRequest):
        logger.debug(f"Попытка login {data.telegram_id}")
        user = await self.uow.user_repository.get_by_field("telegram_id", data.telegram_id)
        if user:
            logger.warn("Пользователь уже существует")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail="Пользователь уже существует"
                )
        user = await self.uow.user_repository.create(telegram_id = data.telegram_id)
        _, access_token = create_access_token(user.id)
        jti, refresh_token = create_refresh_token(user.id)
        session = await self.uow.session_repository.create(
            device_id = data.device_id,
            ip_addres = data.ip_addres,
            refresh_jti = jti,
        )
        logger.debug("Пользователь создан")
        return access_token, refresh_token

            
    async def login(self):
        pass

    async def authorized(self):
        pass

    async def refresh(self):
        pass