from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_login_me_flow():
    email = "user1@example.com"
    password = "strongpass123"

    r = client.post("/auth/register", json={"email": email, "password": password})
    assert r.status_code in (200, 400)

    r = client.post("/auth/token", data={"username": email, "password": password})
    assert r.status_code == 200, r.text
    token = r.json()["access_token"]

    r = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.json()["email"] == email

def test_requires_token():
    r = client.get("/auth/me")
    assert r.status_code == 401
