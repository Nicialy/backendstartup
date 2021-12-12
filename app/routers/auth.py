from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from app.JWTtoken import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from datetime import timedelta
from app.database import Database
from app.hash import verify_password
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=["Authentication"])
db = Database


@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends()):
    useruid = await db.check_login(db, request.username)
    if not useruid:
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
