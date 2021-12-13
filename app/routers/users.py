from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from app.database import Database as db
from app.hash import get_password_hash, verify_password
from app.model import User, UserProfile
from app.oauth2 import get_current_user


router = APIRouter(tags=["profile"])



@router.get('/profile')
async def profile_info(current_user: User = Depends(get_current_user)):

    return await db.take_profile(db, current_user)


@router.put('/profile')
async def change_info(request: UserProfile, current_user: User = Depends(get_current_user)):
    print(request.new_password)
    if  request.new_password :
        if  len(request.new_password) < 6 or request.new_password.isdigit():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Bad password, password shoud be better :)")
        if not verify_password(request.old_password,
                                await db.take_password(db, current_user)):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Incorrect password")
        request.new_password = get_password_hash(request.new_password)
   
    return await db.chang_profile(db, current_user, request)
