import datetime

from model.user import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, ForeignKey, DATETIME
from api.dblink import db_session
from sqlalchemy import select, and_, or_
from sqlalchemy.orm import joinedload
from datetime import datetime
from model.jobtitles import JobTitles
from model.trait import Trait
from model.up_trait import up_trait


class UserProfile(Base):
    __tablename__ = 'lc_user_profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('lc_users.id'))
    jt_id = Column(Integer, ForeignKey('lc_jobtitles.id'))
    firstname = Column(String, nullable=False)
    secondname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    remark = Column(String, nullable=False)
    user = relationship('User', uselist=False, foreign_keys=user_id)
    jt = relationship('JobTitles', uselist=False, foreign_keys=jt_id)
    traits = relationship('Trait', uselist=True, secondary=up_trait)

    @staticmethod
    def add_record(user_profile):
        db = db_session()
        db.add(user_profile)
        db.commit()

    @staticmethod
    def update_record(user_profile_db, new_user_profile):
        db = db_session()
        new_user_profile: UserProfile
        user_profile_db: UserProfile
        if new_user_profile.firstname:
            user_profile_db.firstname = new_user_profile.firstname
        if new_user_profile.lastname:
            user_profile_db.lastname = new_user_profile.lastname
        if new_user_profile.secondname:
            user_profile_db.secondname = new_user_profile.secondname
        if new_user_profile.remark:
            user_profile_db.remark = new_user_profile.remark
        db.add(user_profile_db)
        db.commit()
        return new_user_profile

    @staticmethod
    def get_record_uid(user_id):
        db = db_session()
        smtp = select(UserProfile).where(UserProfile.user_id == user_id)
        user_profile_db = db.scalar(smtp)
        return user_profile_db

    @staticmethod
    def get_all_profiles_join_jobtitles():
        db = db_session()
        smtp = select(UserProfile).options(joinedload(UserProfile.jt))
        profiles_db = db.scalars(smtp).all()
        return profiles_db

    @staticmethod
    def get_record_join_traits(user_profile_id):
        db = db_session()
        smtp = select(UserProfile).options(joinedload(UserProfile.traits)).where(UserProfile.id == user_profile_id)
        user_profile_db = db.scalar(smtp)
        return user_profile_db

    @staticmethod
    def is_have(profile_id):
        db = db_session()
        smtp = select(UserProfile.id).where(UserProfile.id == profile_id)
        profile_db = db.scalar(smtp)
        return profile_db
    @staticmethod
    def get_record_upid(profile_id):
        db = db_session()
        smtp = select(UserProfile).where(UserProfile.id==profile_id)
        profile_db = db.scalar(smtp)
        return profile_db


#
#
# profile = UserProfile(user_id=13, jt_id=1, firstname='test', secondname='test', lastname='test', remark='test')
#
# db = db_session()
# db.add(profile)
# db.commit()
