from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl                                                                # pydantic의 HttpURL을 str 대신하는 타입으로 사용 가능
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []                                                        # tags 속성: str타입으로 이루어진 list 타입으로 구성 
   #tags: set[str] = set()                                                      # set: 중복없는 리스트 만들기 
    image: list[Image] | None = None                                            # 클래스의 속성으로 클래스를 정의할 수 있음(중첩 모델), list로 감싸면 image리스트 안에 Image 클래스의 객체들이 들어간다.

class Offer(BaseModel):
    name:str
    description: str | None = None
    price: float
    items: list[Item]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id" : item_id, "item" : item}
    return results

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

@app.post("/index-weights/")
async def create_index_weights(weights: dict[int,float]):                       # JSON 파일은 key로써 str타입밖에 안 받음. 그러나 fastAPI에서는 int나 float타입을 str타입으로 변환시켜주기 때문에 편하게 사용할 수 있다.
    return weights