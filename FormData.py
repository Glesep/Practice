from typing import Annotated
from fastapi import FastAPI, Form

app = FastAPI()

# Query나 Body에 Form 파라미터 적용 가능
# Form 파라미터 적용시키면 값이 JSON이 아닌 form field로 전송됨
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username" : username}