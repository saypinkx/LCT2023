from model.user import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, ForeignKey
from api.dblink import db_session



class Material(Base):
    __tablename__ = 'lc_material'
    id = Column(Integer, primary_key=True)
    folder_id = Column(Integer, ForeignKey('lc_mat_folder.id'))
    name = Column(String)
    link = Column(String)
    folder = relationship('Folder', uselist=False, foreign_keys=folder_id, back_populates='materials')

    def __init__(self, folder="", name="",
                 link=""):
        self.folder_id = folder
        self.name = name
        self.link = link

    @staticmethod
    def get_record(material_id: int):
        db = db_session()
        material_db = db.query(Material).get(material_id)
        return material_db

    @staticmethod
    def delete_record(material_db):
        db = db_session()
        db.delete(material_db)
        db.commit()

    @staticmethod
    def add_record(db_material):
        db = db_session()
        db.add(db_material)
        db.commit()
        return db_material
    @staticmethod
    def update_record(db_material, new_material):
        db = db_session()
        db_material.link, db_material.name = new_material.link, new_material.name
        db.add(db_material)
        db.commit()
        return db_material



