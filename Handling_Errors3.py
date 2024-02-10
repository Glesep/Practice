from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse                                                                 # JSON 파일 대신 텍스트로 오류를 표현하고 싶을 때 
from starlette.exceptions import HTTPException as StarletteHTTPException                                        # JSON 파일 대신 텍스트로 오류를 표현하고 싶을 때 

app = FastAPI()

@app.exception_handler(StarletteHTTPException)                                                                  # JSON 파일 대신 텍스트로 오류를 표현하고 싶을 때 
async def http_exception_handler(request, exc): 
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")                                    # JSON 파일 대신 텍스트로 오류를 표현하고 싶을 때 
    return {"item_id": item_id}