from typing import Annotated, Literal
from uuid import UUID, uuid4
from beanie import Document, Indexed,Link,init_beanie
from pydantic import EmailStr, Field

from models.Users import Users




class Session(Document):    
    id:UUID=Field(default_factory=uuid4)
    user_id:Link[Users]
    title:str
    

