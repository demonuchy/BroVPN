from typing import Optional, Callable
from fastapi import HTTPException, status
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .db.repository import AUoW
from .schema import UserLoginRequest, ServiceUserLoginRequest
from .serializer import UserModelSerializer
from .utils.sms import generate_session_pair
from .utils.jwt import create_access_token, create_refresh_token

from shared.logger.logger import logger
from shared.database.base import BaseUnitOfWork

class AuthService:
    def __init__(
            self, 
            uow_factory : Optional[Callable[[], type[BaseUnitOfWork]]] = None, 
            user_serializer : Optional[Callable[[], SQLAlchemyAutoSchema]] = None 
            ):
        self._uow = uow_factory() or AUoW()
        self._user_serializer = user_serializer() or UserModelSerializer()
    
    async def login(self, data : ServiceUserLoginRequest):
        pass
        
    async def verefy():
        pass

    async def singin(self):
        pass

    async def authorized(self):
        pass

    async def refresh(self):
        pass