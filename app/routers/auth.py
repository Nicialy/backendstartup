from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from app.JWTtoken import  create_access_token
from datetime import timedelta
from app.database import Database as db
from app.hash import verify_password
from fastapi.security import OAuth2PasswordRequestForm

from app.settings import ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter(tags=["Authentication"])



@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends()):
    user_uid = await db.check_login(db, request.username)
    if not user_uid:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with {request.username} not found")

    if not verify_password(request.password, await db.take_password(db, request.username)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    # generate a jwt token and return
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": request.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
