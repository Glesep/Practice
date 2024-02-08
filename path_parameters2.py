from enum import Enum
from fastapi import FastAPI

# 경로 매개변수로 가능한 값들을 미리 정의 : Enum 사용
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

@app.get("/users/me")                                       #경로 작동은 순차적이므로 명시적인 것부터 먼저 선언함, 변수 먼저 선언하면 "me"를 매개변수로 인식함
async def read_user_me():
    return {"user_id" : "the current user"}

@app.get("/users/{user_id}")                                # {user_id} 먼저 선언하면 "me"를 매개변수의 값으로 인식함
async def read_user(user_id: str):
    return {"user_id" : user_id}

@app.get("/models/{model_name}")                            # Enum을 사용하여 미리 매개변수에 올 값들을 정의할 수 있음
async def get_model(model_name: ModelName):
    # 변수 표현 방법 잘 보기
    # 1.
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    # 2.
    if model_name.value == "resnet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")                         # 매개변수가 경로일 경우 이렇게 정의험, :path는 매개변수가 "경로"가 되어야 함을 명시함
async def read_file(file_path: str):
    return {"file_path" : file_path}
