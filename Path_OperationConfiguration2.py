# 엔드포인트에서 사용할 수 있는 매개변수들
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

@app.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    #description="Create an item with all the information, name, description, price, tax and a set of unique tags"               # description 1
    response_description="The created item"                                                                                      # Response에서 나오는 description, fastAPI 기본 값은 'Successful response'
)
async def create_item(item: Item):                                                                                               # description 2
    """                                                                                                                          
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

@app.get("/elements/", tags=["items"], deprecated=True)                                                                           # deprecated를 엔드포인트에 사용할 수 있음
async def read_elements():
    return [{"item_id", "Foo"}]