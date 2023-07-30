from fastapi import APIRouter, Depends
from structs.auth import (
    RegisterReq,
    RegisterResp
)

router = APIRouter()


@router.post("/register", response_model=RegisterResp)
async def register_router(item: RegisterReq):
    pass
