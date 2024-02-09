from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    
class UserInDB(BaseModel):
    username: str
    hased_password: str
    email: EmailStr
    full_name: str | None = None

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


# .dict(): Pydentic model의 데이터를 딕셔너리 타입으로 만들어 줌
def fake_save_user(user_in: UserIn):
    hased_password= fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in_dict(), hased_password=hased_password)                          # **: 함수를 호출할 때 키워드 인자를 딕셔너리로 전달하는데 사용
    print("User saved! ..not really")
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved