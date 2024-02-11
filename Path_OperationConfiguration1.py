# 엔드포인트에서 사용할 수 있는 매개변수들

from enum import Enum
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

# Enum을 이용한 Tag
class Tags(Enum):
    items = "items"
    users = "users"

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

@app.post("/itmes/", response_model=Item, status_code=status.HTTP_201_CREATED)                  # Status Code를 바로 보낼 수 있다.
async def create_item(item: Item):
    return item

# tags: 각각의 엔드포인트를 Swagger에서 그룹화할 때 사용
@app.post("/items/", response_model=Item, tags=["items"])
async def create_item(item: Item):
    return item

@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]

@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]

# Enum을 이용한 tags 사용
@app.get("/items/", tags=[Tags.itmes])
async def get_items():
    return ["Potal gun", "Plumbus"]

@app.get("/users/", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]