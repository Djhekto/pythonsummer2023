from sqlalchemy.orm import Session
from model import Book
from schemas import Book_sc

def get_book(db:Session,skip:int=0,limit:int=100):
    return db.query(Book).offset(skip).limit(limit).all

def get_book_by_id(db:Session,book_id:int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db:Session,book:Book_sc):
    temp_book = Book(title = book.title, descript =  book.descript)
    db.add(temp_book)
    db.commit()
    db.refresh(temp_book)
    return temp_book

def remove_book(db:Session,b_id:int):
    temp_book = get_book_by_id(db=db,book_id=b_id)
    db.delete(temp_book)
    db.commit()
    
def update_book(db:Session, b_id:int, title:str, description:str):
    temp_book = get_book_by_id(db=db,book_id=b_id)
    temp_book.title = title
    temp_book.descript = description
    db.commit()
    db.refresh(temp_book)
    return temp_book
    


