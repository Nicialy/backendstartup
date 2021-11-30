from fastapi.params import Form
from pydantic import BaseModel, validator
from typing import Optional, Text







class UserProfile(BaseModel):
    
    first_name:str = None
    last_name: str = None
    oldpassword: str = None
    newpassword: str = None
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

class FeedPost(BaseModel):
    Text : str 
    description: str = None
    url :str
class FeedPostShow(BaseModel):
    id: int
    id_user: int
    number_like: int
    Text :str
    description: str = None
    url :str = None

    
    
