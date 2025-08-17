from fastapi import FastAPI
from app.db import create_db_and_tables
from app.routers import auth, users

app = FastAPI(title="fastapi-starter (auth+db)")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/v1", tags=["v1"])

@app.get("/health")
def health():
    return {"status": "ok"}
