from fastapi import APIRouter
from fastapi.param_functions import Depends
from app.database import Database
from app.model import  User, UserProfile
from app.oauth2 import get_current_user


router = APIRouter( tags=["profile"])
db = Database 



@router.get('/profile')
async def profile_info(current_user:User = Depends(get_current_user) ):
    
    return await db.take_profile(db,current_user)
@router.put('/profile')
async def change_info(request: UserProfile,current_user:User = Depends(get_current_user)):

    await db.chang_profile(db,current_user,request)
    return {f"FirstName: {request.first_name} and LastName:{request.last_name} succesful change "}