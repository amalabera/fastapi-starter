# fastapi-starter

Production-ready **FastAPI** skeleton with JWT auth + SQLModel (SQLite), tests, CI, and Docker.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs
```

## Endpoints
- `GET /health`
- `POST /auth/register`  (email, password)
- `POST /auth/token`     (OAuth2 password flow → JWT)
- `GET /auth/me`         (requires Bearer token)
- `GET /v1/whoami`       (requires Bearer token)

## Tests
```bash
pytest -q
```

## Docker
```bash
docker build -t fastapi-starter:dev .
docker run -p 8000:8000 fastapi-starter:dev
```
