from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")                    # 경로 매개변수 설정 : item_id
async def read_item(item_id: int):                   # 함수 인자 : item_id -> 경로 매개변수에서 받아옴, 타입 설정 가능
    return {"item_id" : item_id}