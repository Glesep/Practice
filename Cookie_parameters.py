# 쿠키 파라미터 설정법
from typing import Annotated
from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):                              # Cookie()함수 써주지 않으면 Query로 인식
    return {"ads_id" : ads_id}

