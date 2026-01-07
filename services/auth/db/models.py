import uuid
import enum
from typing import List
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import (String, DateTime, BigInteger, UUID, 
                        Enum, ForeignKey,  func, Text, Boolean, 
                        CheckConstraint, text,)


from .base import AuthBase


class User(AuthBase):
    __tablename__ = "users"
   
    id : Mapped[int]

    phone_number : Mapped[str] = mapped_column(String(11), unique=True, nullable=True)
    hash_password : Mapped[str] = mapped_column(String(20), nullable=True)
    telegram_id : Mapped[str] = mapped_column(String(20), nullable=True, unique=True)

    is_active : Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    last_login : Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    created_at : Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())

    sessions : Mapped[List["UserSession"]] = relationship(
        "UserSession", 
        back_populates="user", 
        cascade="delete-orphan", 
        lazy="selectin"
        )
    

class UserSession(AuthBase):
    __tablename__ = "user_sessions"

    id : Mapped[int]

    device_id : Mapped[str] = mapped_column(String(50), unique=False, nullable=True)
    ip_addres : Mapped[str] = mapped_column(String(15), unique=False, nullable=False)
    refresh_jti : Mapped[uuid.UUID] = mapped_column(UUID, nullable=False, index=True)
    last_activity : Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
    
    user_id : Mapped[int] = mapped_column(
        ForeignKey("auth.users.id", ondelete="CASCADE"), 
        nullable=False, 
        index=True
        )
    user : Mapped["User"] = relationship(
        "User", 
        back_populates="sessions"
        )