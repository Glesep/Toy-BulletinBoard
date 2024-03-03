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

Base = declarative_base()