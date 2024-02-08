# Request 모듈 import 안해서 오류 발생함


from fastapi import FastAPI
from pydantic import BaseModel

# 모델 어트리뷰트가 기본 값을 가지고 있어도 필수 입력 X
class Item(BaseModel):
    name:str
    description: str | None = None                                      # 기본값 None이므로 필수 X
    price: float
    tax: float | None = None                                            # 기본값 None이므로 필수 X

app = FastAPI()

@app.post("/items/")
async def create_item(item_id: int, item: Item, q: str | None = None):  # ** : 함수 호출시에 사용, 딕셔너리 형태로 키워드 인수 전달 가능
    result = {"item_id" : item_id, **item.dict()}                       # 함수 매개변수 : 1. 경로 매개변수와 겹친다면 경로 매개변수로 사용됨  2. 매개변수가 유일한 타입으로 되어있으면 쿼리 매개변수로 사용됨
    if q:                                                               #                3. Pydantic 모델 타입으로 선언되어 있으면 요청 본문으로 해석됨
        result.update({"q" : q})                                        
    return result