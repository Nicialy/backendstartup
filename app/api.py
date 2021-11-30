from fastapi import FastAPI
from app.database import Database
from app.routers import auth
from .routers import users,registr,posts


        
db = Database 
app = FastAPI()



@app.on_event("startup")
async def startup():
    await db.create_pool(db)
    
    
@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await db.close(db)
    
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(registr.router)
app.include_router(posts.router)

