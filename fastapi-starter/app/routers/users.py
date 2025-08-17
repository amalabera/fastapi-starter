from fastapi import APIRouter, Depends
from app.models import User
from app.schemas import UserRead
from app.security import get_current_user

router = APIRouter()

@router.get("/whoami", response_model=UserRead)
def whoami(user: User = Depends(get_current_user)):
    return user
