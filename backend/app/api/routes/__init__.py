from fastapi import APIRouter
from app.api.routes.auths import router as auth_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth")
