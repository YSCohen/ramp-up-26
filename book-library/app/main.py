from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uuid

app = FastAPI()


class book(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    author: str
    year: int


books: dict[str, book] = {}


# Implement a POST request at the /books/ endpoint that takes the title, author, and year in the request body and returns the created book with its assigned id.
@app.post("/books", response_model=book)
def create_book(new_book: book):
    books[new_book.id] = new_book
    return new_book


# Implement a GET request at the /books/ endpoint that returns a list of all books.
@app.get("/books", response_model=list[book])
def list_book_ids():
    return list(books.values())


# Implement a GET request at the /books/{id} endpoint that returns the details of a specific book by id.
@app.get("/book/{id}", response_model=book)
def get_book(id: str):
    book_item = books.get(id)
    if book_item is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_item


# Implement a PUT request at the /books/{id} endpoint that takes the id in the URL and the updated book details in the request body. It should update the book details for the given id.
@app.put("/book/{id}")
def update_book(id: str, new_book: book):
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[id] = new_book


# Implement a DELETE request at the /books/{id} endpoint that deletes the specified book by id.
@app.delete("/book/{id}")
def delete_book(id: str):
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books.pop(id)
