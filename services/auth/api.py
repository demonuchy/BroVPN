from fastapi import APIRouter, status, Header
from fastapi.responses import JSONResponse, Response
from fastapi.requests import Request

from schema import UserLoginRequest, ServiceUserLoginRequest
from depends import ServiceDep


main_router = APIRouter(prefix="/api/v1/auth")


@main_router.post("/login")
async def login(
    request : Request,  
    data : UserLoginRequest, 
    service : ServiceDep, 
    device_id : str | None = Header(None, alias="X-Device-ID")
    ) -> Response:
    """Регистрация в сиситеме"""
    data = ServiceUserLoginRequest(
        device_id=device_id, 
        ip_addres=request.client.host, 
        **data.model_dump()
        )
    access_token, refresh_token = await service.login(data)
    return JSONResponse(
        content={
            "detail" : "Пользователь успешно создан", 
            "data" : {
                "access_token" : access_token,
                "refresh_token" : refresh_token
                }
            }, 
            status_code=status.HTTP_201_CREATED,
            )


@main_router.post("/singin")
async def signin(): 
    """Вход в систему"""


@main_router.post("/authorized")
async def authorized(): 
    """Аунтфикация при каждом запросе"""


@main_router.post("/refresh")
async def refresh(): 
    """Аунгтификация по refresh токену"""
