from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates                                                # 템플릿 사용 가능 모듈
from starlette.staticfiles import StaticFiles
from pydantic import BaseModel                                                   # static file 사용 가능하게 하는 모듈

app = FastAPI()
templates = Jinja2Templates(directory="templates")                                              # 템플릿 사용 가능하게 함 
app.mount("/static", StaticFiles(directory="static"), name="static")                            # static 디렉토리에 있는 파일을 사용 가능하게 함

# 글쓰기 후 서버로 전송된 모델
class Post(BaseModel):
    tilte: str
    content: str
    date: str

@app.get("/")
async def read_root(request: Request):                                                          # templates 디렉토리에 있는 index.html 템플릿을 렌더링 후 request 객체를 템플릿에 전달하여 요청에 대한 정보를 템플릿에서 사용 가능
    return templates.TemplateResponse("index.html", {"request": request})

# 글쓰기를 위한 페이지 보여주기
@app.get("/write/")
async def get_write(request: Request):
    return templates.TemplateResponse("write.html", {"request": request})

# 글쓰기를 위한 정보 보내주기
@app.post("/write/")
async def post_write(post:Post):
    print("hello")


