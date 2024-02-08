from fastapi import FastAPI                 #fastAPI import

secondapp = FastAPI()                       # FastAPI 인스턴스 생성

@secondapp.get("/")                         # 경로 작동 생성(get,post,put...)
async def root():                           # 경로 작동 함수 정의
    return {"Hello": "World"}               # 콘텐츠 반환