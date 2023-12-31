from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, text
from api.dblink import db_session
from . import user_sessions
import datetime, uuid
from api.ini_api import IAPI
from sqlalchemy import select

Base = declarative_base()


class User(Base):
    __tablename__ = 'lc_users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    params = Column(JSON)
    role = Column(String)

    def __init__(self, username="", password="",
                 params="", email="", role=""):
        self.username = username
        self.password = password
        self.email = email
        self.params = params
        self.role = role

    @staticmethod
    def add_record(obj):
        dbs = db_session()
        dbs.add(obj)
        dbs.commit()

    @staticmethod
    def delete_record(user_db):
        db = db_session()
        db.delete(user_db)
        db.commit()

    @staticmethod
    def get_record(user_id):
        db = db_session()
        user_db = db.query(User).get(user_id)
        return user_db

    @staticmethod
    def update_record(user_db, new_user):
        db = db_session()
        new_user_dict = new_user.dict()
        for key in new_user_dict:
            if not new_user_dict[key]:
                new_user_dict[key] = user_db.__dict__[key]
        user_db.username, user_db.password, user_db.email, user_db.params, user_db.role = \
            new_user_dict[
                'username'], new_user_dict[
                'password'], new_user_dict['email'], new_user_dict['params'], new_user_dict['role']
        db.add(user_db)
        db.commit()
        return new_user

    @staticmethod
    def get_all_records():
        db = db_session()
        users_db = db.query(User).all()
        return users_db

    @staticmethod
    def is_have(user_id):
        db = db_session()
        smtp = select(User.id).where(User.id == user_id)
        return db.scalar(smtp)

    @staticmethod
    def do_login(usname, paword):
        sess = db_session()
        # mdpass = md5(paword.encode('utf-8')).hexdigest()
        mdpass = paword
        our_user = sess.query(User).filter((User.username == usname) & (User.password == mdpass)).first()
        if not our_user:
            return 'invalid', ''

        sess.flush()
        sql = text("delete from lc_sessions where user_id = :us_id")
        db_session().execute(sql, {'us_id': our_user.id, })

        sess_uid = str(uuid.uuid4())
        user_session = user_sessions.User_Sessions()
        user_session.user_id = our_user.id
        user_session.sess_id = sess_uid
        user_session.last_check = datetime.datetime.now()
        sess.add(user_session)
        sess.commit()
        return sess_uid, our_user.role

    @staticmethod
    def un_login():
        m = IAPI.US
        s = db_session()
        s.delete(m)
        s.commit()

    @staticmethod
    def current_user():
        sess = db_session()
        m = IAPI.US
        m2 = sess.query(User).filter((User.id == m.user_id)).first()
        return m2

    @staticmethod
    def check_session(token):
        sess = db_session()
        user_session = sess.query(user_sessions.User_Sessions).filter_by(sess_id=token).first()
        if user_session:

            if user_session.last_check < datetime.datetime.now() - datetime.timedelta(days=5):
                sql = text("delete from lc_sessions where sess_id = :sess_id")
                sess.execute(sql, {'sess_id': user_session.sess_id, })
                sess.commit()
                return None
            user_session.last_check = datetime.datetime.now()
            sess.commit()
            return user_session
        return None

    def __repr__(self):
        return "<User_Registration('%s)>" \
            % (self.username)


user = User()
