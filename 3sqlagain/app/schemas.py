from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
#from pydantic.generics import GenericModel
#https://github.com/pydantic/pydantic/issues/858  didnt help  GenericModel->BaseModel => suc??

T = TypeVar("T")

class Book_sc(BaseModel):
    id: Optional[int]=None
    title: Optional[str]=None
    descript: Optional[str]=None

    class Config:
        orm_mode = True

class Request(BaseModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestBook(BaseModel):
    parameter: Book_sc = Field(...)

class Response (BaseModel,Generic[T]):
    code: str
    status: str
    msg: str
    res: Optional[T]
