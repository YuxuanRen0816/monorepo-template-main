from fastapi import FastAPI, Query, Path

app = FastAPI()

# GET API without parameters
@app.get("/books/")
def read_books():
    return {"message": "List of all books"}

# GET API with path parameters
@app.get("/books/{book_id}")
def read_book_by_id(book_id: int):
    return {"book_id": book_id}

# GET API with query parameters
@app.get("/books/by_category/")
def read_books_by_category(category: str):
    return {"category": category}

# GET API with path and query parameters
@app.get("/books/{book_id}/details/")
def read_book_details(book_id: int, author: str = Query(None)):
    return {"book_id": book_id, "author": author}

# POST API
@app.post("/books/")
def create_book(name: str):
    return {"name": name, "message": "Book created"}

# PUT API
@app.put("/books/{book_id}")
def update_book(book_id: int, name: str):
    return {"book_id": book_id, "name": name, "message": "Book updated"}

# DELETE API
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    return {"book_id": book_id, "message": "Book deleted"}
