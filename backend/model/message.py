import datetime

from model.user import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, ForeignKey, DATETIME
from api.dblink import db_session
from sqlalchemy import select, and_, or_
from sqlalchemy.orm import joinedload
from datetime import datetime


class Message(Base):
    __tablename__ = 'lc_messages'
    id = Column(Integer, primary_key=True)
    from_id = Column(Integer, ForeignKey('lc_users.id'))
    to_id = Column(Integer, ForeignKey('lc_users.id'))
    date = Column(DATETIME, default=datetime.utcnow())
    after_id = Column(Integer, ForeignKey('lc_messages.id'))
    topic = Column(String)
    body = Column(String)
    is_completed = Column(Integer)
    is_read = Column(Integer)
    sender = relationship('User', uselist=False, foreign_keys=from_id)
    recipient = relationship('User', uselist=False, foreign_keys=to_id)
    after = relationship('Message', uselist=False, foreign_keys=after_id, remote_side=[id])

    @staticmethod
    def add_record(message):
        db = db_session()
        db.add(message)
        db.commit()

    @staticmethod
    def get_record(message_id):
        db = db_session()
        message_db = db.query(Message).get(message_id)
        return message_db

    @staticmethod
    def delete_record(message_db):
        db = db_session()
        db.delete(message_db)
        db.commit()

    @staticmethod
    def update_record(message_db, new_message):
        message_db: Message
        if new_message.topic is None:
            new_message.topic = message_db.topic
        if new_message.body is None:
            new_message.body = message_db.body
        message_db.topic, message_db.body, message_db.is_completed, message_db.is_read = new_message.topic, new_message.body, new_message.is_complited, message_db.is_read
        return new_message

    @staticmethod
    def is_have(message_id):
        db = db_session()
        smtp = select(Message.id).where(Message.id == message_id)
        return db.scalar(smtp)

    @staticmethod
    def get_dialog(user1_id, user2_id):
        db = db_session()
        smtp = select(Message).where(or_(and_(Message.from_id == user1_id, Message.to_id == user2_id),
                                         and_(Message.from_id == user2_id, Message.to_id == user1_id)))
        messages_db = db.scalars(smtp).all()
        return messages_db

#
# message = db_session().query(Message).get(1)
# print(message.sender)
#
# message_new = Message(from_id=1, to_id=200, topic='', body='', is_completed=1, is_read=1)
# db_session().add(message_new)
# db_session().commit()
