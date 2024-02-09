# 리턴 타입 결정: 반환 데이터 검사, JSON 스키마에 추가, 보안을 위함
# 리턴 타입과 response_model을 같이 사용하는 경우, 후자가 우선순위에 있음
from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

@app.post("/items/")
async def create_item(item: Item) -> Item:                                  # 리턴 타입 = Item 클래스 
    return item

@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name= "Potal Gun", price= 42.0),
        Item(name= "Plumbus", price=32.0)
    ]


# 정해진 타입과 다른 데이터를 리턴받고 싶을 때, response_model -> 필터링 역할을 함 / ex) 딕셔너리 또는 데이터베이스 객체를 받고 싶은데 그것들이 Pydantic model 안에 정의되어 있을 때
@app.post("/items_UseRM/", response_model=Item)                             
async def create_item(item: Item) -> Any:
    return item

@app.get("/items_UseRM/", response_model=list[Item])
async def read_items() -> Any:
    return [
        Item(name= "Potal Gun", price= 42.0),
        Item(name= "Plumbus", price=32.0)
    ]

# 이렇게 하면 절대 안됨!!!
@app.post("/user_NEVERUSE/")
async def create_user(user: UserIn) -> UserIn:                                      # 유저를 만들 때마다 유저의 "패스워드를 포함하고 있는" UserIn의 객체들의 결과값들이 반환됨 -> 취약점 생성
    return user

@app.post("/user_OK/", response_model=UserOut)                                      # UserOut을 response_model로 썼기 때문에 password가 없는 유저 정보만 리턴됨 (필터링 역할, 타입 검사는 불가)
async def create_user(user: UserIn) -> Any:
    return user



