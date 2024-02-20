from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

user_name = "yoon"                                                                              # 데이터베이스 사용자 이름
user_pwd = "1234"                                                                               # 데이터베이스 사용자 비밀번호
db_host = "127.0.0.1:3306"                                                                      # 데이터베이스 호스트
db_name = "bulletinboard"                                                                       # 데이터베이스 이름(mysql: 스키마 이름)

DATABASE = "mysql+pymysql://%s:%s@%s/%s?charset=utf8" % (                                       # DB URL
    user_name,
    user_pwd,
    db_host,
    db_name,
)

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True,
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE,
    )
)



# def execute_query(query):                                                                       # 쿼리 실행 함수
#     with ENGINE.connect() as connection:                                                        # with: 특정 작업 수행 전 리소스를 할당하고 작업이 끝난 후에는 리소스를 자동으로 정리(쿼리 실행 후 연결을 자동으로 닫기 위해), as: 앞에 있는 객체를 변수 connect에 할당시킴 
#         result = connection.excute(text(query))
#         return result.fetchall()                                                                # fetchall(): 결과 실행 후 결과에 해당하는 모든 행 불러옴

Base = declarative_base()