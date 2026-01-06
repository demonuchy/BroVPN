from pydantic import BaseModel, Field


class ServiceRegisterMixin(BaseModel):
    ip_addres : str = Field(..., max_length=16, min_length=7)
    device_id : str = Field(default=None)


class UserRegisterWithTelegramRequest(BaseModel):
    telegram_id : str = Field(...)


class ServiceUserLoginWithTelegramRequest(UserRegisterWithTelegramRequest, ServiceRegisterMixin):
    pass


class UserLoginWithTelegramRequest(UserRegisterWithTelegramRequest):
    pass


class UserRegisterRequest(BaseModel):
    phone_number : str = Field(..., min_length=11, max_length=11)
    password : str = Field(..., min_length=6, max_length=20)


class ServiceUserRegisterRequest(UserRegisterRequest, ServiceRegisterMixin):
    pass


class UserLoginRequest(UserRegisterRequest):
    pass