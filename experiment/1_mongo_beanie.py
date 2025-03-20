import os
from motor.motor_asyncio import AsyncIOMotorClient

from dotenv import load_dotenv

load_dotenv()
from typing import Annotated, Literal
from uuid import UUID, uuid4
from beanie import Document, Indexed,Link,init_beanie
from pydantic import EmailStr, Field



class Users(Document):
    id:UUID=Field(default_factory=uuid4)
    name:str
    email:Annotated[EmailStr, Indexed(unique=True)]
    password:str
    verified:bool=False
    role:Literal['user','privilaged','admin']='user'
    
class Session(Document):    
    id:UUID=Field(default_factory=uuid4)
    user_id:Link[Users]
    title:str

async def init_db():
    client=AsyncIOMotorClient(os.getenv('MONGO_URL'))
    
    await init_beanie(database=client.db_name, document_models=[Session,Users],multiprocessing_mode=True)





# async def get_session(id:str)->Session:
#     session=await Session.get(id)
#     return session

# async def store_session(id:UUID, userId:str, Title:str)->Session:
#     return await Session(id=id, user_id=userId, title=Title).insert()

# async def store_user(name:str,email:str,password:str,role:str)->Users:
#     return await Users(name=name,email=email,password=password,role=role).insert()

# async def get_user(email:str=None)->Users:
#     user = await Users.find_one(Users.email==email)
#     return user

# async def login_user(email:str,password:str)->Users:
#     user = await Users.find_one(Users.email==email,Users.password==password)
#     return user

