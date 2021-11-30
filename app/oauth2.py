from fastapi import Depends
from fastapi import HTTPException,status
from fastapi.security import OAuth2PasswordBearer

from pydantic.typing import NONE_TYPES
from app.JWTtoken import ALGORITHM, SECRET_KEY, verify_token




oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentails_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return verify_token(token, credentails_exception)