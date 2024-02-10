from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# 커스텀 예외상황 핸들러 만들기
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()

@app.exception_handler(UnicornException)
# Request와 예외를 매개변수로 받음
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."}
    )

@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}
