from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import create_db_and_tables
from app.routers import auth, users

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

# 👇 Serve Swagger UI at the root ("/")
app = FastAPI(
    title="fastapi-starter (auth+db)",
    lifespan=lifespan,
    docs_url="/",
    redoc_url=None,
)

@app.get("/health")
def health():
    return {"status": "ok"}

# Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/v1", tags=["v1"])
