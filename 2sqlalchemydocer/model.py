from typing import Optional,List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
import datetime as dt
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
#https://www.youtube.com/watch?v=2X8B_X2c27Q&t=1311s
import db as _db

class Contact(_db.Base):
    __tablename__ = "contacts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    first_name = _sql.Column(_sql.String, index=True)
    last_name = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, index=True, unique=True)
    phone = _sql.Column(_sql.String, index=True, unique=True)
    date_created = _sql.Column(_sql.DateTime, default=dt.datetime.utcnow,index=True, unique=True)
    




"""
class cl_gender(str,Enum):
    male = "male"
    fe = "fe"
    
class cl_role(str,Enum):
    admin = "admin"
    neadmin = "neadmin"

class user(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    aaa: Optional[str]
    gender: cl_gender 
    roles: List[cl_role]

class userUpdateReq(BaseModel):
    name: Optional[str]    
    aaa: Optional[str]
    gender: Optional[cl_gender]
    roles: Optional[List[cl_role]]
"""