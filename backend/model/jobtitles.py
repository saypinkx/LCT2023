from model.user import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, ForeignKey, DATETIME
from api.dblink import db_session
from sqlalchemy import select, and_, or_
from sqlalchemy.orm import joinedload
from datetime import datetime


class JobTitles(Base):
    __tablename__ = 'lc_jobtitles'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    descr = Column(String)
