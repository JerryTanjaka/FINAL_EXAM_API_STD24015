from fastapi import FastAPI
from starlette.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Characteristics(BaseModel):
    ram_memory: int
    rom_memory: int

class phones(BaseModel):
    identifier: str
    brand: str
    model : str
    characteristics: Characteristics

@app.get("/ping")
def root():
    return JSONResponse(content={"message": "pong"}, status_code=200)

@app.get("/health")
def health():
    return JSONResponse(content={"status": "ok"}, status_code=200)
