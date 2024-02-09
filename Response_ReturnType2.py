# 리턴 타입 결정: 반환 데이터 검사, JSON 스키마에 추가, 보안을 위함
# 리턴 타입과 response_model을 같이 사용하는 경우, 후자가 우선순위에 있음
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str

@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:                            # 상속을 통해 필터링과 타입 검사까지 수행
    return user




