from pydantic import BaseModel, Field

class UserLoginRequest(BaseModel):
    phone_number : str = Field(..., min_length=11, max_length=11)
    password : str = Field(..., min_length=6, max_length=20)

class ServiceUserLoginRequest(UserLoginRequest):
    ip_addres : str = Field(..., max_length=16, min_length=7)
    device_id : str = Field(default=None)

class UserSinginRequest(UserLoginRequest):
    pass