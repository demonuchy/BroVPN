from sqlalchemy.ext.asyncio import AsyncSession

from .models import  User, UserSession
from .context import session_factory

from shared.database.base import BaseRepository, BaseUnitOfWork


class UserRepository(BaseRepository[User]):
    def __init__(self, session : AsyncSession):
        super().__init__(session=session, model=User)


class UserSessionRepository(BaseRepository[UserSession]):
    def __init__(self, session : AsyncSession):
        super().__init__(session=session, model=UserSession)


class AUoW(BaseUnitOfWork):
    
    # Добавляем анннотации просто для удобства разработки 
    # IDE будет подсказывать
    user_repository : 'UserRepository'
    session_repository : 'UserSessionRepository'

    def __init__(self):
        super().__init__(session_factory=session_factory, schema="auth")
        self.add_repo("user", UserRepository)
        self.add_repo("session", UserSessionRepository)

