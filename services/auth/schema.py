from pydantic import BaseModel, Field

class UserLoginRequest(BaseModel):
    phone_number : str = Field(..., min_length=11, max_length=11)
    password : str = Field(..., min_length=6, max_length=20)

class ServiceUserLoginRequest(UserLoginRequest):
    ip_addres : str
    device_id : str

class UserSinginRequest(UserLoginRequest):
    pass