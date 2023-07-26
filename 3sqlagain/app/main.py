#https://www.youtube.com/watch?v=d_ugoWsvGLI
from fastapi import FastAPI
import model
from config import engine
import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def ff1():
    return "FF1"

app.include_router(router.router,prefix="/book",tags=["book"])

