from model.user import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, ForeignKey
from api.dblink import db_session
from model.material import Material

class Folder(Base):
    __tablename__ = 'lc_mat_folder'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('lc_mat_folder.id'))
    name = Column(String)
    descr = Column(String)
    parent = relationship('Folder', uselist=False, foreign_keys=parent_id, remote_side=[id])
    materials = relationship('Material', uselist=True, back_populates='folder')

    def __init__(self, parent="", name="",
                 descr=""):
        self.parent = parent
        self.name = name
        self.descr = descr

    @staticmethod
    def add_record(folder_db):
        db = db_session()
        db.add(folder_db)
        db.commit()
        return folder_db

    @staticmethod
    def get_record(folder_id):
        db = db_session()
        db_folder = db.query(Folder).get(folder_id)
        return db_folder

    @staticmethod
    def delete_record(folder_db):
        db = db_session()
        db.delete(folder_db)
        db.commit()

    @staticmethod
    def update_record(folder_db, new_folder):
        db = db_session()
        folder_db: Folder
        folder_db.name, folder_db.descr = new_folder.name, new_folder.descr
        db.add(folder_db)
        db.commit()
        return new_folder
