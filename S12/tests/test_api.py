import pytest
from fastapi.testclient import TestClient
from fastapi import status
from s12.main import api

@pytest.fixture(scope="session")
def client():
    return TestClient(api)

def test_api_create_task(client):
    response=client.post("/task")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() is not None