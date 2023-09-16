from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    year: int

    def __init__(self, id, title, author, description, rating, year) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.year = year


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    description: str
    rating: int = Field(gt=-1, lt=11)
    year: int = Field(gt=0, lt=2024)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Book Title",
                "author": "Author's Name",
                "description": "Description of the Book",
                "rating": 5,
                "year": 2023
            }
        }



BOOKS = [
    Book(1, 'Book1', 'Author1', 'Description1', 10, 2010),
    Book(2, 'Book2', 'Author2', 'Description2', 9, 2011),
    Book(3, 'Book3', 'Author3', 'Description3', 8, 2012),
    Book(4, 'Book4', 'Author4', 'Description4', 7, 2013),
    Book(5, 'Book5', 'Author5', 'Description5', 6, 2021),
    Book(6, 'Book6', 'Author5', 'Description6', 5, 2023),
    Book(7, 'Book7', 'Author4', 'Description7', 4, 2020),
    Book(8, 'Book8', 'Author3', 'Description8', 3, 2008),
    Book(9, 'Book9', 'Author2', 'Description9', 2, 2023),
    Book(10, 'Book10', 'Author1', 'Description10', 1, 2021)
]

def create_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book


@app.get("/books")
def get_all_books():
    return BOOKS


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get("/books/")
def get_book_by_rating(rating: int):
    b = []
    for book in BOOKS:
        if book.rating == rating:
            b.append(book)
    
    return b


@app.get("/books/search/")
def get_book_by_year(year: int):
    b = []
    for book in BOOKS:
        if book.year == year:
            b.append(book)

    return b


@app.post("/add_book")
def add_book(requested_book: BookRequest):
    book = Book(**requested_book.model_dump())
    BOOKS.append(create_book_id(book))


@app.put("/books/update_book")
def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.delete("/books/delete/{book_id}")
def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)