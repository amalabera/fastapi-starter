from fastapi import FastAPI, APIRouter

app = FastAPI(title="fastapi-starter")

router = APIRouter(prefix="/v1", tags=["v1"])

@router.get("/echo")
def echo(msg: str):
    return {"echo": msg}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router)
