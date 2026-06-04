from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int = 0
    title: str
    author: str
    year: int


next_id: int = 1
books: dict[int, Book] = {}


# Implement a POST request at the /books/ endpoint that takes the title, author,
# and year in the request body and returns the created book with its assigned
# id.
@app.post("/books/", response_model=Book)
def create_book(new_book: Book):
    global next_id
    new_book.id = next_id
    books[next_id] = new_book
    next_id += 1
    return new_book


# Implement a GET request at the /books/ endpoint that returns a list of all
# books.
@app.get("/books/", response_model=list[Book])
def list_books():
    return list(books.values())


# Implement a GET request at the /books/{id} endpoint that returns the details
# of a specific book by id.
@app.get("/books/{id}", response_model=Book)
def get_book(id: int):
    book_item = books.get(id)
    if book_item is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_item


# Implement a PUT request at the /books/{id} endpoint that takes the id in the
# URL and the updated book details in the request body. It should update the
# book details for the given id.
@app.put("/books/{id}", response_model=Book)
def update_book(id: int, new_book: Book):
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    new_book.id = id
    books[id] = new_book
    return new_book


# Implement a DELETE request at the /books/{id} endpoint that deletes the
# specified book by id.
@app.delete("/books/{id}", response_model=Book)
def delete_book(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books.pop(id)
