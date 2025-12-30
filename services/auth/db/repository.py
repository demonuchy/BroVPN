from sqlalchemy.ext.asyncio import AsyncSession

from shared.database.base import BaseRepository, BaseUnitOfWork
from .models import  User, UserSession
from  db.context import session_factory


class UserRepository(BaseRepository[User]):
    def __init__(self, session : AsyncSession):
        super().__init__(session=session, model=User)


class UserSessionRepository(BaseRepository[UserSession]):
    def __init__(self, session : AsyncSession):
        super().__init__(session=session, model=UserSession)


class AUoW(BaseUnitOfWork):
    def __init__(self):
        super().__init__(session_factory=session_factory, schema="auth")
        self.add_repo("user", UserRepository)
        self.add_repo("session", UserSessionRepository)