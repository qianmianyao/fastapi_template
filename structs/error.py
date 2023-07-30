from pydantic import BaseModel


class ErrorResp(BaseModel):
    error: str
    message: str
    code: int
