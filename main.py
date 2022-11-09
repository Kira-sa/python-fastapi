from fastapi import FastAPI
import uvicorn
from mylib.logic import do_magic

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Try call /magic"}


@app.get("/magic/{name}")
async def magic(name: str):
    """Page for some magic"""

    result = do_magic(name)
    return {"result": result}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host="127.0.0.1")
