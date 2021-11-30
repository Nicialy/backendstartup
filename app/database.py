import asyncpg
from app.model import User, UserProfile
class Database():

    async def create_pool(self):
        
             self.pool = await asyncpg.create_pool(dsn='postgres://lxvlturrusqxai:6df017459f27f15d1c78b68ab3ee7668f1664b0b80bd6852a945c2c5b7fe4e26@ec2-34-242-89-204.eu-west-1.compute.amazonaws.com:5432/dd5hmevb94p9bq')
             print("Connection to PostgreSQL DB successful")

    async def create_user(self, User: User):

        await self.pool.execute(f'''
        INSERT INTO users (login,password) VALUES ('{User.login}','{User.password}');
        ''')
    async def close(self):
           await self.pool.close()
           print("Connecting Close")
    async def check_login(self, login: str):
            userlogin = await self.pool.fetchrow(f"""
             SELECT uid FROM users WHERE login = '{login}';       
                """)
            return userlogin
    async def take_password(self, login:str):
        password = await self.pool.fetchval(f"""
             SELECT password FROM users WHERE login = '{login}';       
                """)
        return password
    async def take_profile(self,login:str):
        userprofile = UserProfile
        userprofile = await self.pool.fetch(f"""
             SELECT first_name,last_name FROM users WHERE login = '{login}';       
                """)
        return userprofile
    async def chang_profile(self,login:str,userprofile: UserProfile):
        await self.pool.execute(f"""
            UPDATE users set first_name='{userprofile.first_name}' , last_name='{userprofile.last_name}' where login='{login}';
        """)
    


