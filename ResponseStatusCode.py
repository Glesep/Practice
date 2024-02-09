from fastapi import FastAPI, status

app = FastAPI()

# status_code=: HTTP status code 정의 파라미터
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

# fastapi.status import하면 외우지 않고 편하게 정의 가능 
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}