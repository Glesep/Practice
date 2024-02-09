from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type: str = "car"

class PlaneItem(BaseItem):
    type: str = "plane"
    size: int

# 위의 클래스를 상속받음
items = {
    "item1" : {"description" : "All my friends drive a low rider", "type" : "car"},
    "item2" : {
        "description" : "Music is my aeroplane",
        "type" : "plane",
        "size" : 5
    }
}

# response_model에서 상속받은 것들 명시
@app.get("/items/{item_id}", response_model=Union[PlaneItem,CarItem])                               # response_model= PlaneItem | CarItem -- 오류 발생함
async def read_item(item_id: str):
    return items[item_id]


