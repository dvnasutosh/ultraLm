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
    