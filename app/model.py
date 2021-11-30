from pydantic import BaseModel
from typing import Optional







class UserProfile(BaseModel):
    
    first_name:str
    last_name: str
class User(BaseModel):
    login : str
    password: str
    

class LoginUser(BaseModel):
        login:str
        password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    login: Optional[str] = None