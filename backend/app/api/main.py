from fastapi import APIRouter

from app.api.routes.connections import connections_router
from app.api.routes.home import home_router
from app.api.routes.login import login_router
from app.api.routes.users import users_router

api_router = APIRouter()
api_router.include_router(login_router, prefix="/auth/login", tags=["login"])
api_router.include_router(users_router, prefix="/auth/users", tags=["users"])
api_router.include_router(connections_router, prefix="/connections", tags=["friends"])
api_router.include_router(home_router, prefix="/home", tags=["hub"])
