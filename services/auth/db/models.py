import uuid
import enum
from typing import List
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, DateTime, BigInteger, UUID, Enum, ForeignKey,  func, Text
from .base import AuthBase


class User(AuthBase):
    __tablename__ = "users"

    phone_number : Mapped[str] = mapped_column(unique=True, nullable=False)
    hash_password : Mapped[str] = mapped_column(nullable=False)

    sessions : Mapped[List["UserSession"]] = relationship(
        "UserSession", 
        back_populates="user", 
        cascade="delete-orphan", 
        lazy="selectin"
        )

class UserSession(AuthBase):
    __tablename__ = "user_sessions"

    device_id : Mapped[str] = mapped_column(String(50), unique=False, nullable=True)
    ip_addres : Mapped[str] = mapped_column(String(15), unique=False, nullable=False)
    user_id : Mapped[int] = mapped_column(ForeignKey("auth.users.id", ondelete="CASCADE"), nullable=False, index=True)

    user : Mapped["User"] = relationship(
        "User", 
        back_populates="sessions"
        )