from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from typing import List
from starlette.middleware.cors import CORSMiddleware

from db import session #, execute_query
from models import DBTable, Data

import datetime

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

# cursor = session.cursor()                                                                           # 커서는 세션이랑 연결, 커서 이용해서 sql의 쿼리 실행 가능

@app.get("/")
async def do_redirect():
    return RedirectResponse(url="/index")

# INDEX
@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    context= {}
    data = session.query(DBTable).all()

    context["request"]  = request                                                                   # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
    context["data"]     = data

    return templates.TemplateResponse("index.html", context)

# READ
@app.get("/index/{index}", response_class=HTMLResponse)
async def index(request: Request, index: int):
    context= {}
    data = session.query(DBTable).filter(DBTable.id == index).first()

    context["request"]  = request                                                                   # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
    context["title"]    = data.title
    context["time"]     = data.time
    context["contents"] = data.contents

    return templates.TemplateResponse("read.html", context)

# CREATE (자동으로 현재 시간 추가) 완성!
@app.get("/write", response_class=HTMLResponse)
async def write(request: Request):                                                                  # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
    context={}
    context["request"] = request                                                                    # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함

    query_makerow = "INSERT INTO bb (id, title, time, contents) VALUES ()"
    return templates.TemplateResponse("write.html", context)

@app.post("/write")
async def create_data(data: Data):
    datalist = list(data)

    d_title = datalist[0][1]
    d_contents = datalist[1][1]
    d_time = datetime.datetime.now()

    data = DBTable()
    data.title = d_title
    data.contents = d_contents
    data.time = d_time

    session.add(data)
    session.commit()

    return "게시글이 저장되었습니다."


# UPDATE
@app.get("/update", response_class=HTMLResponse)
async def update(request: Request):                                                                  # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
    context={}
    context["request"] = request                                                                    # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
    return templates.TemplateResponse("update.html", context)


# DELETE
@app.get("/delete", response_class=HTMLResponse)
async def update(request: Request):                                                                  # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
    context={}
    context["request"] = request                                                                    # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
    return templates.TemplateResponse("delete.html", context)