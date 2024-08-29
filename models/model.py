from pydantic import BaseModel

class CodeRequest(BaseModel):
    language: str
    code: str

class CodeResponse(BaseModel):
    status: str
    formatted_code: str
    language: str