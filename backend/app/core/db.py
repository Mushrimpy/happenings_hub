from sqlmodel import Session, create_engine, select
from app.api.services import auth_svc
from app.core.config import settings
from app.models import User, UserCreate

engine = create_engine(settings.DB_URI)


def init_db(session: Session) -> None:
    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = auth_svc.create_user(session=session, user_create=user_in)
