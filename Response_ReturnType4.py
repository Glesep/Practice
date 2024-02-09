# 인스턴스에서 명시되지 않은 속성들을 JSON 파일로 보내고 싶지 않을 때
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydentic 모델 정의
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

# Pydantic 모델을 딕셔너리 형태로 인스턴스화(기본적인 파이썬의 클래스에서 인스턴스 생성과는 다름)
items = {
    "foo" : {"name": "Foo", "price" : 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []}
}
    
# response_model_exclude_unset=true: 인스턴스에 명시되지 않은 속성들은 제외시킴 
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str): 
    return items[item_id]

# 위의 방법의 shortchut (추천하진 않음)
@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"}          # set값으로 변수를 받음, list나 tuple로 정의해도 FastAPI가 set값으로 자동변환
)
async def read_item_name(item_id: str):
    return items[item_id]

@app.get("/items/{item_id}/public",
        response_model=Item,
        response_model_exclude={"tax"}                      # set값으로 변수를 받음, list나 tuple로 정의해도 FastAPI가 set값으로 자동변환
)
async def read_item_public_data(item_id: str):
    return items[item_id]