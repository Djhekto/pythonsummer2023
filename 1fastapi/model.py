from typing import Optional,List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class cl_gender(str,Enum):
    male = "male"
    fe = "fe"
    
class cl_role(str,Enum):
    admin = "admin"
    neadmin = "neadmin"

class user(BaseModel):
    id: Optional[UUID] = uuid4()
    #print(str(id))
    name: str
    aaa: Optional[str]
    gender: cl_gender 
    roles: List[cl_role]

class userUpdateReq(BaseModel):
    name: Optional[str]    
    aaa: Optional[str]
    gender: Optional[cl_gender]
    roles: Optional[List[cl_role]]
