from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db import create_db_and_tables
from app.routers import auth, users

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables at startup
    create_db_and_tables()
    yield

app = FastAPI(title="fastapi-starter (auth+db)", lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}

# Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/v1", tags=["v1"])
