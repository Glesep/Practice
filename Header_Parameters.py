# 헤더 파라미터 설정법
from typing import Annotated
from fastapi import Header, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):                               # Header()함수 써주지 않으면 Query로 인식
    return {"User-Agent" : user_agent}

@app.get("/items_NoConvert_Underscores")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None                     # Header에서는 -로 분류되곤 하는데, python에서는 -가 허용되지 않는다.
):                                                                                                      # 따라서 FastAPI에선 _를 -로 자동 변환하고 있는데, 변환하고 싶지 않은 경우엔 convert_underscorces=False 적용하자
    return {"strange_header" : strange_header}

@app.get("/items_DuplicateHeaders/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):                            # 다수의 x_token 헤더를 전송할 경우, 리스트 형식으로 전송
    return {"X-Token values" : x_token}