import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert response.json() == {"message": "List of all books"}

def test_read_book_by_id():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == {"book_id": 1}

def test_read_books_by_category():
    response = client.get("/books/by_category/?category=fiction")
    assert response.status_code == 200
    assert response.json() == {"category": "fiction"}
