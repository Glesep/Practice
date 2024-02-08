from typing import Annotated, Union
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

# examples=[]
class Item(BaseModel):
    name: str                                            
    description: str | None = None
    price: float 
    tax: float | None = None

# Body()에서 example value 넣기(openapi_examples() 함수 이용) 다수의 example value 넣을 수 있지만 표시되는 건 상단의 하나 뿐임.
@app.put("/items/{item_id}")
async def update_item(
    item_id: int, 
    item: Annotated[
        Item, 
        Body(                                                                 
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name" : "Foo",
                        "description" : "A very nice Item",
                        "price" : 35.4,
                        "tax" : 3.2
                    }
                }
                "converted":
            }
        )
    ]
):
    results = {"item_id" : item_id, "item" : item}
    return results