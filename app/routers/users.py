from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from app.database import Database
from app.hash import get_password_hash, verify_password
from app.model import User, UserProfile
from app.oauth2 import get_current_user


router = APIRouter(tags=["profile"])
db = Database


@router.get('/profile')
async def profile_info(current_user: User = Depends(get_current_user)):

    return await db.take_profile(db, current_user)


@router.put('/profile')
async def change_info(request: UserProfile, current_user: User = Depends(get_current_user)):

    if request.newpassword is not None:
        if not verify_password(request.oldpassword,
                               await db.take_password(db, current_user)):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Incorrect password")
        request.newpassword = get_password_hash(request.newpassword)
    return await db.chang_profile(db, current_user, request)
