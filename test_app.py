from fastapi.testclient import TestClient
from web import app  # adjust this import if needed

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello world"
