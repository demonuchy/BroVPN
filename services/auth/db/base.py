from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import BigInteger, func
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr


class AuthBase(AsyncAttrs, DeclarativeBase):
    """..."""
    __abstract__ = True

    id : Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())

    @declared_attr
    def __table_args__(cls):
        """ВСЕ модели auth service в схеме 'auth'"""
        return {'schema': 'auth'}
    


    

