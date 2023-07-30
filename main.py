import uvicorn
from fastapi import FastAPI
from apis.v1 import auth

app = FastAPI()
app.include_router(router=auth.router, prefix="/v1/auth", tags=["auth"])

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8080, reload=True, workers=6)
