import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_book():
    response = client.post("/books/", json={"name": "Test Book", "category": "fiction"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Book", "category": "fiction"}

def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Test Book", "category": "fiction"}]

def test_get_book_by_id():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Book", "category": "fiction"}

def test_update_book():
    response = client.put("/books/1", json={"name": "Updated Book", "category": "non-fiction"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Updated Book", "category": "non-fiction"}

def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

