from typing import Annotated, Union
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

# examples=[]
class Item(BaseModel):
    name: str = Field(examples=["Foo"])                                             # OpenAPI에서 속성의 예시(example value)를 달아줌
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])

    '''
    # example 한번에 생성 
    model_config = {
        "json_schema_extra" : {
            "examples": [                                                           
                {
                    "name" : "Foo",
                    "description" : "A very nice Item",
                    "price" : 35.4,
                    "tax" : 3.2
                }
            ]
        }
    }
'''


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id" : item_id, "item" : item}
    return results