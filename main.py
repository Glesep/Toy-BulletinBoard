from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from typing import List
from starlette.middleware.cors import CORSMiddleware

from db import session 
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



@app.get("/")
async def do_redirect():
    return RedirectResponse(url="/index")

# INDEX 완성!
@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    context= {}
    data = session.query(DBTable).all()

    context["request"]  = request                                                                   # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
    context["data"]     = data

    return templates.TemplateResponse("index.html", context)

# READ 완성!
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

   
    return templates.TemplateResponse("write.html", context)

@app.post("/write")
async def create_data(data: Data):
    datalist = list(data)                                                                           # pydantic 모델을 변수에 저장

    d_title = datalist[0][1]
    d_contents = datalist[1][1]
    d_time = datetime.datetime.now()

    data = DBTable()                                                                                # DBTable(): DBTable 객체 생성
    data.title = d_title
    data.contents = d_contents
    data.time = d_time

    session.add(data)                                                                               # 세션에 ORM을 저장
    session.commit()                                                                                # 세션 commit함으로써 DB에 ORM 반영

    return "게시글이 저장되었습니다."


# UPDATE 완성!
@app.get("/update/{index}", response_class=HTMLResponse)
async def update(request: Request, index: int):                                                                 # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
    context= {}
    data = session.query(DBTable).filter(DBTable.id == index).first()

    context["request"]  = request                                                                               # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
    context["title"]    = data.title
    context["time"]     = data.time
    context["contents"] = data.contents

    return templates.TemplateResponse("update.html", context)

@app.put("/update/{index}")
async def update_data(data: Data, index: int):
    datalist = list(data)
    d_title = datalist[0][1]
    d_contents = datalist[1][1]
    d_time = datetime.datetime.now()

    data = session.query(DBTable).filter(DBTable.id == index).first()
    data.title = d_title
    data.contents = d_contents
    data.time = d_time

    session.commit()

    return "게시글이 수정되었습니다."
   


# DELETE
@app.delete("/delete/{index}")
async def delete_data(data: Data, index: int):                                                                  # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
   
    session.query(DBTable).filter(DBTable.id == index).delete()
    session.commit()                                                                                            # 템플릿에서 request 객체를 받아와 요청에 대한 정보를 다루게 함
    