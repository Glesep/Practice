from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder                                               # JSON파일에서 호환이 되도록 해주는 모듈
from pydantic import BaseModel

fake_db = ()

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None

app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)                                      #Pydantic model -> dict, datetime -> str
    fake_db[id] = json_compatible_item_data