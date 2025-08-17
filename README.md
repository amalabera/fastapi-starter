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
