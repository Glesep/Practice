from typing import Annotated
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None 


@app.put("/items_body_1/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None                                                                                # body 매개변수는 클래스 타입으로 정의 가능하다.
):
    results = {"item_id" : item_id}
    if q:
        results.update({"q" : q})
    if item:
        results.update({"item" : item})
    return results

@app.put("/items_body_2/{item_id}")
async def update_item(                                                                                      # body 매개변수가 2개 이상 정의될 때 딕셔너리 자료형으로 저장됨(키: 필드 네임)
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]                                # 값이 하나밖에 없는 변수(일반적으로 쿼리변수로 인식됨)인데 Body 매개변수로 정의하고 싶을 때: Annotated[x, Body()] 
    ):                                                                                                      # 
    results = {"item_id": item_id, "item": item, "user": user}
    return results

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):                               # body 매개변수가 하나밖에 없는데 딕셔너리 자료형으로 저장을 원함 -> Body(embed=True)
    results= {"item_id" : item_id, "item":item}
    return results

