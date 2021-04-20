from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "word"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True, debug=True)
