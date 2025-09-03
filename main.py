from fastapi import FastAPI
from starlette.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Characteristics(BaseModel):
    ram_memory: int
    rom_memory: int

class phones(BaseModel):
    identifier: str
    brand: str
    model : str
    characteristics: Characteristics
phones_mempory :List[phones] = []

@app.get("/ping")
def root():
    return JSONResponse(content={"message": "pong"}, status_code=200)

@app.get("/health")
def health():
    return JSONResponse(content={"status": "ok"}, status_code=200)

@app.post("/phones")
def create_phone(list_phones: phones):
    phones_mempory.extend(list_phones)
    return phones_mempory

@app.get("/phones")
def get_phones():
    return phones_mempory

@app.get("/phones/{id}")
def get_phone_by_id(identifier: str):
    for phone in phones_mempory:
        if phone.identifier == identifier:
            return phone
    return JSONResponse(content={"message": "id does not exist or not found"}, status_code=404)


@app.put("/phones/{id}/characteristics")
def update_characteristics(identifier: str, new_characteristics: Characteristics):
    for i, phone in enumerate(phones_mempory):
        if phone.identifier == identifier:
            phones_mempory[i].characteristics = new_characteristics
            return {"message": "characteristics updated", "phones": phones_mempory[i].characteristics}
    return JSONResponse(content={"message": "id does not exist or not found"}, status_code=404)