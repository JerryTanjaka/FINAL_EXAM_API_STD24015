from fastapi import FastAPI
from starlette.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Characteristics(BaseModel):
    ram_memory: int
    rom_memory: int

class Phones(BaseModel):
    identifier: str
    brand: str
    model : str
    characteristics: Characteristics
phones_memory :List[Phones] = []

@app.get("/health")
def health():
    return JSONResponse(content={"status": "ok"}, status_code=200)

@app.post("/phones")
def create_phone(list_phones: List[Phones]):
    phones_memory.extend(list_phones)
    return phones_memory

@app.get("/phones")
def get_phones():
    return phones_memory

@app.get("/phones/{id}")
def get_phone_by_id(identifier: str):
    for phone in phones_memory:
        if phone.identifier == identifier:
            return phone
    return JSONResponse(content={"message": "id does not exist or not found"}, status_code=404)


@app.put("/phones/{id}/characteristics")
def update_characteristics(identifier: str, new_characteristics: Characteristics):
    for i, phone in enumerate(phones_memory):
        if phone.identifier == identifier:
            phones_memory[i].characteristics = new_characteristics
            return {"message": "characteristics updated" , "phones": phones_memory[i] + phones_memory[i].characteristics}
    return JSONResponse(content={"message": "id does not exist or not found"}, status_code=404)