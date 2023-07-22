#https://www.youtube.com/watch?v=GN6ICac3OXY
#http://localhost:8000/
#http://localhost:8000/docs
#http://localhost:8000/redoc
from fastapi import FastAPI, HTTPException
from typing import Optional,List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from model import user,cl_gender,cl_role,userUpdateReq

app = FastAPI()

db: List[user] = [
    user(id=uuid4(), name="asd0", aaa = None, gender= cl_gender.male, roles=[cl_role.admin, cl_role.neadmin]),
    user(id=UUID("6283df63-c281-4ac4-81b3-ff20d7c4b9ce"), name="JHJhjnm", aaa = None, gender= cl_gender.fe, roles=[cl_role.neadmin])
] 

@app.get("/")
def ff1():
    return {"name": "1"}

#http://localhost:8000/111
@app.get("/111")
async def get_users():
    return db

#http://localhost:8000/111 post in rest client json user type in body
@app.post("/111")
async def register_user(newuser: user):
    db.append(newuser)
    return {"id": newuser.id}

@app.delete("/111/{user_id}")
async def delete_user(user_id: UUID):
    for user_ in db:
        if user_.id == user_id:
            db.remove(user_)
            return
    #not found
    raise HTTPException(
        status_code=404,#422 validation error
        detail=f"user with id: {user_id} does not exist"
    )

#@app.put("/111/{user_id, newuserinfo}")
#async def update_user(user_id: UUID, newuserinfo: user):

#http://localhost:8000/111/46b57e83-83e7-49ac-be9a-ef39fa36c2d7
@app.put("/111/{user_id}")
async def update_user(user_id: UUID, user_update: userUpdateReq):
    for user_ in db:
        if user_.id == user_id:
            if user_update.name is not None:
                user_.name = user_update.name
            if user_update.aaa is not None:
                user_.aaa = user_update.aaa
            if user_update.gender is not None:
                user_.gender = user_update.gender
            if user_update.roles is not None:
                user_.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

"""
@app.get("/")
async def ff1():
    temp1 = await ff2()
    return {"name": "1"}

def ff2():
    return None
    """