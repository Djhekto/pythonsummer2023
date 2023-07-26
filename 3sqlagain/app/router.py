from fastapi import APIRouter,HTTPException,Path,Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Book_sc,RequestBook,Response
import crud


router = APIRouter()

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close

@router.post('/create')
async def create(req: RequestBook, db:Session=Depends(get_db)):
    crud.create_book(db,book=req.parameter)
    return Response(code=200,status="ok",msg="b created suc").dict(exclude_none = True)

@router.get('/')
async def get(db:Session=Depends(get_db)):
    temp_book = crud.get_book(db,0,100)
    return Response(code=200,status="ok", msg = "Suc all fetch", result = temp_book).dict(exclude_none = True)

@router.get("/{id}")
async def get_by_id(id:int,db:Session = Depends(get_db)):
    temp_book = crud.get_book_by_id(db,id)
    return Response(code=200,status="ok", msg = "suc data by id", result = temp_book).dict(exclude_none = True)

@router.get("/{id}")
async def update_book(req:RequestBook, db:Session = Depends(get_db)):
    temp_book = crud.update_book(db,b_id= req.parameter.id,
                                 title=req.parameter.title,
                                 description=req.parameter.descript)
    return Response(code=200,status="ok", msg = "suc upd data", result = temp_book)
  
@router.delete("/{id}")
async def delete(id:int, db:Session = Depends(get_db)):
    crud.remove_book(db,b_id=id)
    return Response(code=200, status="ok", msg = "suc del smt").dict(exclude_none = True)
















