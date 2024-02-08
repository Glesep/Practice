from typing import Annotated, Union
from fastapi import FastAPI, Query

app = FastAPI()

# 기본값이 None인 경우

# 1. Annotated 없는 코드_1
@app.get("/items_nonAnnotated_1/")
async def read_items(q: str | None = Query(default=None, max_length=50)):                                   # 기본값이 들어간 경우(None 포함) 필수 입력 X
    results = {"items" : [{"item_id" : "Foo"}, {"item_id" : "Bar"}]}                                        # str이 기본값일 때: q: str = Query(default="Yoon")
    if q:
        results.update({"q" : q})
    return results

# 2. Annotated 없는 코드_2
@app.get("/items_nonAnnotated_2/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):                             # 기본값이 들어간 경우(None 포함) 필수 입력 X
    results = {"items" : [{"item_id" : "Foo"}, {"item_id" : "Bar"}]}
    if q:
        results.update({"q" : q})
    return results

# 3. Annotated 있는 코드
@app.get("/items_Annotated/")
async def read_items(                                                                                       # q : Annotated[str | None] = None -> q 라는 파라미터에 문자열 또는 None이 들어갈 수 있음. 기본값은 None임.
    q: Annotated[str | None, Query(min_length=3, max_length = 50, pattern = "^fixedquery$")] = None         # pattern: 정규표현식
    ):                                                                                                      # str이 기본값일 때: Annotated[str | None, Query(max_length = 50)] = "Yoon" 
    results = {"items" : [{"item_id" : "Foo"}, {"item_id" : "Bar"}]}                                        
    if q:
        results.update({"q" : q})
    return results

@app.get("/items_required/")
async def read_items(q: Annotated[str, Query(min_length=3)]):                                               # 동일한 표현법 -> q: Annotated = ... 
    results = {"items" : [{"item_id" : "Foo"}, {"item_id" : "Bar"}]}                                        
    if q:
        results.update({"q" : q})
    return results

@app.get("/items_list_1/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):                                       # 리스트로 쿼리를 받고 싶을 때 사용 / 현재 API 문서에서는 리스트 적용이 안됨
    query_items = {"q" : q}
    return query_items

@app.get("/items_list_2/")
async def read_items(q: Annotated[list[str] | None, Query()] = ["Foo", "Bar"]):                             # 리스트로 기본값 설정
    query_items = {"q" : q}
    return query_items

@app.get("/items_list_3/")
async def read_items(q: Annotated[list, Query] = []):                                                       # 이렇게도 정의 가능. 하지만 이렇게 정의 시, list의 내용을 검증하진 않음 
    query_items = {"q" : q}
    return query_items

@app.get("items_etc/")
async def read_items(
    q: Annotated[
        str | None,
        Query(                                                                                              # 아래는 쿼리의 설정에 관한 것들임
            alias="item-query",                                                                             # 이 쿼리의 별칭 설정 
            title="Query String",                                                                           # 쿼리 제목 설정
            description="This is my description",                                                           # 쿼리 설명 설정
            min_length=3,                                                                                   # 쿼리 최소 길이 설정
            max_length=50,                                                                                  # 쿼리 최대 길이 설정
            pattern="^fixedquery$",                                                                         # 쿼리에 정규표현식 설정
            deprecated=True                                                                                 # 쿼리 사용 유무 설정
        )
    ] = None
):
    results = {"items" : [{"item_id" : "Foo"}, {"item_id" : "Bar"}]}
    if q:
        results.update({"q" : q})
    return results

@app.get("/items_hiddenQuery/")                                                                             
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None                              # include_in_schema=False: 문서에서 특정 쿼리를 제외하고 싶을 때 사용. 경로 자체에도 사용 가능                     
):  
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}