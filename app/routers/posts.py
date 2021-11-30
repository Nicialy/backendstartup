from typing import Optional
from fastapi import APIRouter,UploadFile,File
from fastapi.param_functions import Body, Form, Query
from starlette.requests import Request
from app.oauth2 import get_current_user
from fastapi.param_functions import Depends
from app.database import Database
from app.model import FeedPost,User




router = APIRouter( tags=["feed"])
db =Database

#,response_model= FeedPost,response_model_exclude_unset=True - чтобы yt возращать  пармаетры с null
@router.post('/feed')
async def create_post(body: FeedPost,current_user:User = Depends(get_current_user)) :
    
    await db.create_post(db,current_user,body)  
    return {"News successfully published"} 

@router.get('/feed')
async def alltake_posts(section: Optional[str] = None):
        if section == 'recomended':
                posts= await db.take_recomededpost(db)
                return posts
        posts= await db.take_post(db)
        return posts


@router.get('/feed?section=recomended')
async def recomeded_posts():
        pass