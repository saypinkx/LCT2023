from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def db_connect():
    return Mydb.connect


def db_session():
    return Mydb.bdsession


def db_engine():
    return Mydb.engine


class Db:
    def __init__(self):
        self.cstring = 'mysql+pymysql://admin_lct2023:1232023@185.221.152.242/admin_lct2023'
        self.engine = create_engine(self.cstring)
        self.bdsession = sessionmaker(bind=self.engine, autoflush=False)()
        self.connect = self.engine.connect()


Mydb = Db()
