import datetime

from model.user import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, ForeignKey, DATETIME
from api.dblink import db_session
from sqlalchemy import select, and_, or_
from sqlalchemy.orm import joinedload
from datetime import datetime
from model.up_trait import up_trait


class Trait(Base):
    __tablename__ = 'lc_traits'
    id = Column(Integer, primary_key=True)
    group_name = Column(String, nullable=False)
    trait_name = Column(String, nullable=False)
    trait_text = Column(String, nullable=False)
    group_code = Column(Integer, nullable=False)
    users = relationship('UserProfile', uselist=True, secondary=up_trait)

    @staticmethod
    def get_type_record():
        db = db_session()
        smtp = select(Trait.group_name, Trait.group_code).distinct()
        traits_db = db.scalars(smtp).all()
        return traits_db

    @staticmethod
    def get_record(trait_id):
        db = db_session()
        smtp = select(Trait).where(Trait.id == trait_id)
        trait_db = db.scalar(smtp)
        return trait_db

    @staticmethod
    def is_have(trait_id):
        db = db_session()
        smtp = select(Trait.id).where(Trait.id == trait_id)
        trait_db = db.scalar(smtp)
        return trait_db

    # @staticmethod
    # def get_statistic(jt_id):
    #     smtp = select(Trait.name).where
