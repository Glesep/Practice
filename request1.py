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
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict