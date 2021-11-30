from fastapi import APIRouter
from app.database import Database




router = APIRouter( tags=["feed"])
db =Database


#@router.post('/feed')
