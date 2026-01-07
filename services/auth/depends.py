from typing import Annotated
from fastapi import Depends

from buisnes import AuthService
from db.repository import AUoW
from serializer import UserModelSerializer


async def _get_service():
    return AuthService(
        uow_factory=AUoW,
        user_serializer=UserModelSerializer
        )

ServiceDep = Annotated[AuthService, Depends(_get_service)]


