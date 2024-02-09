from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()
# Return type으로 Response를 지정한 경우: RedirectResponse와 JSONResponse는 Response 함수를 상속받고 있기 때문에 가능 
@app.get("/portal/")
async def get_portal(teleport: bool = False) -> Response:                               # Return Type Annotation
    if teleport:
        return RedirectResponse(url="https//www.youtube.com/")
    return JSONResponse(content={"message" : "Here's your interdimensional portal."})

# Return type으로 Response의 자식 class인 RedirectResponse를 지정한 경우: FastAPI에서 자동으로 처리
@app.get("/teleport/")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://youtube.com/")

# Pydantic type이 아닌 객체를 Return type으로 지정했을 때, 자동적으로 FastAPI에서 Pydantic response model을 만든다.  
# 이 경우에는 type annotation이 1. Pydantic type이거나 2. Response 클래스 또는 그 자식 클래스(한 뿌리?)가 아니기 때문에 오류가 난다. 
@app.get ("/portal_Error/")
async def get_portal(teleport: bool = False) -> Response | dict:     # <- Union
    if teleport: 
        return RedirectResponse(url="https//www.youtube.com/")
    return JSONResponse(content={"message" : "Here's your interdimensional portal."})

# 위의 오류를 막기 위해서는 response_model이 자동적으로 생성되지 않게 만들면 된다. (response_model=None)
@app.get ("/portal_NoError/", response_model=None)          
async def get_portal(teleport: bool = False) -> Response | dict:    
    if teleport: 
        return RedirectResponse(url="https//www.youtube.com/")
    return JSONResponse(content={"message" : "Here's your interdimensional portal."})


