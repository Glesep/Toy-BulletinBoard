from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from typing import List
from starlette.middleware.cors import CORSMiddleware

from db import session
from models import DBTable, Data

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],                                                                            # 모든 도메인에서의 요청 허용
    allow_credentials=True,                                                                         # 인증 정보를 포함한 요청 허용
    allow_methods=["*"],                                                                            # 모든 HTTP methods 허용
    allow_headers=["*"],                                                                            # 모든 HTTP headers 허용
)

# INDEX
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context= {}
    data = session.query(DBTable).all()

    context["request"]  = request
    context["data"]     = data

    return templates.TemplateResponse("index.html", context)

# READ
@app.get("/{index}", response_class=HTMLResponse)
async def index(request: Request, index: int):
    context= {}
    data = session.query(DBTable).filter(DBTable.id == index).first()

    context["request"]  = request
    context["title"]    = data.title
    context["time"]     = data.time
    context["contents"] = data.contents

    return templates.TemplateResponse("read.html", context)

# CREATE
    


# UPDATE
    



# DELETE