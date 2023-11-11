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
from sqlalchemy import text
from sqlalchemy import text


class UserProfile(Base):
    __tablename__ = 'lc_user_profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('lc_users.id'))
    jt_id = Column(Integer, ForeignKey('lc_jobtitles.id'))
    firstname = Column(String, nullable=False)
    secondname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    remark = Column(String, nullable=False)
    is_primer = Column(Integer)
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
        smtp = select(UserProfile).where(UserProfile.id == profile_id)
        profile_db = db.scalar(smtp)
        return profile_db

    @staticmethod
    def add_traits(user_profile, traits_id):
        db = db_session()
        for trait_id in traits_id:
            trait_db = Trait.get_record(trait_id)
            user_profile.traits.append(trait_db)
        db.add(user_profile)
        db.commit()

    @staticmethod
    def get_static(jt_id):
        db = db_session()
        smtp = text(
            f"SELECT t.trait_name, count(*) as weight, (select t2.group_name from lc_traits t2 where t2.trait_name = t.trait_name limit 1) as what FROM lc_traits t, lc_up_traits upt, lc_user_profiles up WHERE t.id = upt.trait_ID and up.id = upt.up_id and up.is_primer = 1 and up.jt_id = {jt_id} group by 1 order by 3, 2 desc")
        rows = db.execute(smtp)
        result = []
        for row in rows:
            result.append([row[0], row[1], row[2]])
        return result

    @staticmethod
    def get_rating(profile_id, jt_id):
        db = db_session()
        smtp = text(
            f"select sum(w) FROM (SELECT r1.trait_id, (SELECT count(*) as weight FROM  lc_traits t, lc_up_traits upt, lc_user_profiles up WHERE t.id = upt.trait_ID and up.id = upt.up_id and up.is_primer = 1 and up.jt_id = {jt_id} and t.id = r1.trait_id) as w FROM lc_up_traits r1  where r1.up_id = {profile_id}) as yt")
        rows = db.execute(smtp)
        result = []
        for row in rows:
            result.append(row[0])

        return result[0]

    @staticmethod
    def get_is_ideal(profile_id, jt_id):
        db = db_session()
        smtp = text(
            f"SELECT  (SELECT count(*) FROM lc_up_traits t1, lc_up_traits t2 where t1.trait_id = t2.trait_id and t1.up_id = up1.id and t2.up_id = {profile_id}) as bliz, up1.lastname FROM lc_user_profiles up1 where up1.jt_id = {jt_id} and up1.is_primer = 1 group by up1.lastname")
        rows = db.execute(smtp)
        result = []
        for row in rows:
            result.append([row[0], row[1]])
        return result

    @staticmethod
    def get_plan(profile_id, jt_id, porog):
        db = db_session()
        smtp = text(f"SELECT t.id, t.trait_name cx FROM lc_traits t, lc_up_traits upt, lc_user_profiles up WHERE t.id = upt.trait_ID and up.id = upt.up_id and up.is_primer = 1 and up.jt_id = {jt_id}  and t.group_code = 3 group by 1 having count(*)>{porog} and t.id not in (select tx.id from lc_traits tx, lc_up_traits t1 where t1.trait_id = tx.id and t1.up_id = {profile_id})")
        rows = db.execute(smtp)
        result = []
        for row in rows:
            result.append([row[0], row[1]])
        return result

#
#
# profile = UserProfile(user_id=13, jt_id=1, firstname='test', secondname='test', lastname='test', remark='test')
#
# db = db_session()
# db.add(profile)
# db.commit()
