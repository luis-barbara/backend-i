#Create a test file named test_main.py:

from fastapi.testclient import TestClient
from src.s11.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI API!"}

def test_create_item_success():
    response = client.post("/items/", json={"name": "Test Item", "price": 15.90, "is_offer": False})  
    assert response.status_code == 200
    assert "item_id" in response.json()
    assert response.json()["item"]["name"] == "Test Item"

def test_create_item_failure():
    response = client.post("/items/", json={})  
    assert response.status_code == 422  

def test_delete_item_success():
    create_response = client.post("/items/", json={"name": "To be deleted", "price": 15.90, "is_offer": True})
    assert create_response.status_code == 200
    item_id = create_response.json()["item_id"]
    delete_response = client.delete(f"/items/{item_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": f"Item {item_id} deleted", "deleted_item": {"name": "To be deleted", "price": 15.90, "is_offer": True}}

def test_delete_nonexistent_item():
    response = client.delete("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"