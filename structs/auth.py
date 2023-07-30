from pydantic import BaseModel


class RegisterReq(BaseModel):
    username: str
    password: str


class RegisterResp(BaseModel):
    uid: int
    username: str
    token: str
