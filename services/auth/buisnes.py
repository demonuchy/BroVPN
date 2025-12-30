from typing import Optional, Callable
from fastapi import HTTPException, status
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from db.repository import AUoW
from schema import UserLoginRequest, ServiceUserLoginRequest
from shared.logger.logger import logger
from shared.database.base import BaseUnitOfWork
from serializer import UserModelSerializer
from utils.jwt import create_access_token, create_refresh_token

class AuthService:
    def __init__(
            self, 
            uow_factory : Optional[Callable[[], type[BaseUnitOfWork]]] = None, 
            user_serializer : Optional[Callable[[], SQLAlchemyAutoSchema]] = None 
            ):
        self._uow = uow_factory() or AUoW()
        self._user_serializer = user_serializer() or UserModelSerializer()
    
    async def login(self, data : ServiceUserLoginRequest):
        logger.debug(f"Попытка входа :{data.phone_number} - {data.password} - {data.ip_addres}")
        async with self._uow.readonly() as u:
            user = await u.user_ropository.get_by_field("phone_number", data.phone_number)
        if user:
            logger.warn("Пользователь уже существует")
            raise HTTPException(detail="Пользователь уже существует", status_code=status.HTTP_409_CONFLICT)
        
    async def verefy():
        pass

    async def singin(self):
        pass

    async def authorized(self):
        pass

    async def refresh(self):
        pass