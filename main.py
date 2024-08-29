from typing import Union

from fastapi import FastAPI
from models.model import CodeRequest,CodeResponse
#importing formating functions
from formater.formater import format_python,format_c,format_java

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/format")
async def format_code(request:CodeRequest)->CodeResponse:
    print(request.code)
    if request.language == "python":
        formate_code = format_python(request.code)
    elif request.language == "c":
        formate_code = format_c(request.code)
    elif request.language == "java":
        formate_code = format_java(request.code)
    else:
        raise Exception(f"Unsupported language: {request.language}")
    
    return {
        "status": "success",
        "formatted_code":formate_code,
        "language":request.language
    }