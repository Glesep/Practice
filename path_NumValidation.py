from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],                                           # 경로 매개변수는 항상 필수 입력, 기본값을 정의해도 필수 입력해야 함.
    q: Annotated[str | None, Query(alias="item-query")] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q" : q})
    return results

@app.get("/item_nonAnnotated_1/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):                           # 기본값이 있는 매개변수는 기본값이 없는 매개변수의 뒤에서 정의되어야 함.(Annotated 미사용시)
    results = {"item_id": item_id}
    if q:
        results.update({"q" : q})
    return results

@app.get("/item_nonAnnotated_2/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):                        # 순서 바꾸려면 앞에 * 입력
    results = {"item_id": item_id}
    if q:
        results.update({"q" : q})
    return results

@app.get("/item_Annotated/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")], q: str                                    # Annotated 사용시 순서 상관 안써도 됨
):
    results = {"item_id": item_id}
    if q:
        results.update({"q" : q})
    return results

@app.get("/item_NumValidations/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1, le=1000)], q: str                              # ge: 이상, gt: 초과, le: 이하, lt: 미만 / ge=1, le=1000: 1 이상 1000 미만  -> int, float값 전부 가능
):
    results = {"item_id": item_id}
    if q:
        results.update({"q" : q})
    return results