from typing import Union
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name" : "Foo"}, {"item_name" : "Bar"}, {"item_name" : "Baz"}]


@app.get("/items/")                                                                              # 경로 매개변수가 아닌 다른 함수 매개변수를 선언하면 "쿼리 매개변수"로 자동 해석
async def read_item(skip: int = 0, limit: int = 10):                                             # 쿼리 매개변수는 URL의 일부이므로 기본 문자열로 선언된다. 하지만 타입 선언을 명시적으로 한 경우, 해당 타입으로 변환 및 검증됨.                         
    return fake_items_db[skip : skip + limit]                                                    # 기본값 -> skip : 0, limit : 10 / 쿼리를 직접 적지 않으면 기본값으로 쿼리 값이 유지된다.

# 경로 시작시 앞에 "/" 꼭 붙이기!!
@app.get("/users/{user_id}/items/{item_id}")
async def read_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False                  # Union[x,y] : 어떤 값이 x나 y 타입임을 명시, None이 들어가면 값이 없을 수 있음을 명시, 기본값이 존재(None 포함)하면 필수 입력 X
    ):                                                                                           # 경로 매개변수와 쿼리 매개변수를 동시에 선언 가능하며 특정 순서로 선언할 필요 X, 매개변수들은 이름으로 감지
    item = {"item_id" : item_id, "owner_id" : user_id}
    if q:
        item.update({"q" : q})
    if not short:
        item.update(
            {"description" : "This is an amazing item that has a long description"}
        )
    return item



