from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_returns_hello_world():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello World"}

def test_health_status():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status":"OK"}