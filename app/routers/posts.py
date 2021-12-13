from typing import Optional
from fastapi import APIRouter

from starlette.requests import Request
from app.oauth2 import get_current_user
from fastapi.param_functions import Depends
from app.database import Database as db
from app.model import FeedPost, User


router = APIRouter(tags=["feed"])



@router.post('/feed')
async def create_post(body: FeedPost, current_user: User = Depends(get_current_user)):

    await db.create_post(db, current_user, body)
    return {"News successfully published"}


@router.get('/feed')
async def alltake_posts(section: Optional[str] = None):
    if section == 'recomended':
        posts = await db.take_recomededpost(db)
        return posts
    posts = await db.take_post(db)
    return posts
