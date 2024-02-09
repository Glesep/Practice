from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

# File(): Form()에서 상속받음. 따라서 File들은 Form 데이터로 업로드가 될 것
@app.post("/files/")
async def create_file(file: Annotated[bytes | None, File(description="A file read as bytes")] = None):
    if not file:
        return {"message" : "No file sent"}
    else:
        return {"file_size" : len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: Annotated[None, UploadFile, File(description="A file read as UploadFile")] = None):
    if not file:
        return {"message" : "No upload file sent"}
    else:
        return {"filename" : file.filename}
# ============================================================================================================================================================================================
    
# 다수의 파일 동시에 업로드할 시 list사용
@app.post("/Multiple_files/")
async def create_files(files: Annotated[list[bytes], File(description="Multiple files as bytes")]):
    return {"file_sizes": [len(file) for file in files]}

@app.post("/Multiple_Uploadfiles/")
async def create_upload_file(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ]
 ):
    return {"filenames" : [file.filename for file in files]}

@app.get("/")
async def main():
    content = """
<body>
<form action = "/files/" enctype="multipart/form-data" method="post">
<input name = "files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)