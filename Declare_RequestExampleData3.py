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

# Body()에서 example value 넣기(openapi_examples() 함수 이용) 다수의 example value 넣을 수 있고 표시도 다 됨.
# **이게 최신**
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
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price 'strings' to actual 'numbers' automatically",
                    "value": {
                        "name": "bar",
                        "price": "35.4"
                    }
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four"
                    }
                }
            }
        )
    ]
):
    results = {"item_id" : item_id, "item" : item}
    return results