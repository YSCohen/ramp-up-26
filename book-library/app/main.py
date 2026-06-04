from fastapi import FastAPI, HTTPException, Response
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
@app.post("/books/", response_model=Book, status_code=201)
def create_book(new_book: Book, response: Response):
    global next_id
    new_book.id = next_id
    books[next_id] = new_book
    next_id += 1
    response.headers["Location"] = f"/books/{new_book.id}"
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
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[id]


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
