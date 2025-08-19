# fastapi-starter (auth+db)

Production-ready FastAPI starter with **JWT auth** (OAuth2 password flow), **SQLModel + SQLite**, tests, and GitHub Actions CI.

![CI](https://github.com/amalabera/fastapi-starter/actions/workflows/ci.yml/badge.svg)

---

## Features
- **Auth**: `/auth/register`, `/auth/token`, `/auth/me` (JWT bearer)
- **Protected sample**: `/v1/whoami`
- **DB**: SQLModel on SQLite (switchable via `DATABASE_URL`)
- **Docs**: Swagger at `/docs` (OpenAPI 3.1)
- **Tests**: `pytest -q` (runs in CI)

## Tech Stack
FastAPI • SQLModel • Pydantic • Python-JOSE • Passlib (bcrypt) • Pytest • GitHub Actions

## Project Layout
app/
main.py
db.py
models.py
schemas.py
security.py
routers/
auth.py
users.py
tests/
test_health.py
test_auth.py
.github/workflows/ci.yml
requirements.txt
# fastapi-starter (auth+db)

FastAPI starter with JWT auth, SQLModel/SQLite, tests, and CI.

## Run (PowerShell)
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
.\.venv\Scripts\python.exe -m pip install "bcrypt<4" --only-binary=:all:
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:SECRET_KEY = "some-long-random-string"
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs

## Endpoints
- POST /auth/register, POST /auth/token, GET /auth/me
- GET /v1/whoami (protected)
- GET /health

Open:

Swagger: http://127.0.0.1:8000/docs

Health: http://127.0.0.1:8000/health

Minimal env vars

SECRET_KEY (required) — long random string for signing JWTs

DATABASE_URL (optional) — defaults to sqlite:///./app.db

Token header: Authorization: Bearer <access_token>
Default expiry: 60 minutes (see ACCESS_TOKEN_EXPIRE_MINUTES in app/security.py)
"Status: health endpoint added."
