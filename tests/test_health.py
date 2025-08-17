from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_echo():
    r = client.get("/v1/echo", params={"msg": "hi"})
    assert r.status_code == 200
    assert r.json()["echo"] == "hi"
