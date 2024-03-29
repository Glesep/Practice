from typing import Annotated
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

# File(), Form() 함수 동시에 정의
@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()]
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type
    }