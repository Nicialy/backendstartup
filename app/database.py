import asyncpg
from app.model import FeedPost, User, UserProfile
from app.settings import DATABASE_URL


class Database:

    async def create_pool(self):

        self.pool = await asyncpg.create_pool(dsn=DATABASE_URL)
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

    async def take_password(self, login: str):
        password = await self.pool.fetchval(f"""
                 SELECT password FROM users WHERE login = '{login}';
        """)
        return password

    async def take_profile(self, login: str):
        userprofile = UserProfile
        userprofile = await self.pool.fetch(f"""
                SELECT first_name,last_name FROM users WHERE login = '{login}';
        """)
        return userprofile

    async def chang_profile(self, login: str, userprofile: UserProfile):
        strback = ""
        if userprofile.first_name is not None:
            await self.pool.execute(f"""
                        UPDATE users set first_name='{userprofile.first_name}' where login='{login}';
            """)
            strback += f" {userprofile.first_name} succeful change"
        if userprofile.last_name is not None:
            await self.pool.execute(f"""
                         UPDATE users set last_name='{userprofile.last_name}' where login='{login}';
            """)
            strback += f" {userprofile.last_name} succeful change"
        if userprofile.new_password:
            await self.pool.execute(f"""
                        UPDATE users set password='{userprofile.new_password}' where login='{login}';
            """)
            strback += f" password succeful change"
        if not strback:
            strback = " Nothing to do"
        return strback

    async def create_post(self, login: str, body: FeedPost):
        uid = await self.pool.fetchval(f"""
                         SELECT uid FROM users WHERE login = '{login}'
        """)

        await self.pool.execute(f'''
                     INSERT INTO post (id_user,number_like,Textz,description,url) VALUES ({uid},0,'{body.text_post}','{body.description}','{body.url}');
        ''')

    async def take_post(self):
        return await self.pool.fetch(f'''
            SELECT * FROM post
        ''')

    async def take_recomededpost(self):
        post = await self.pool.fetch(f"""
            SELECT * FROM POST order by  number_like DESC;
        """)
        return post
