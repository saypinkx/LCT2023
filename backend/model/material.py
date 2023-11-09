from model.user import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, ForeignKey
from api.dblink import db_session
from sqlalchemy import select
from sqlalchemy.orm import joinedload


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
        if new_material.link is not None:
            db_material.link = new_material.link

        if new_material.name is not None:
            db_material.name = new_material.name
        db.add(db_material)
        db.commit()
        return db_material

    @staticmethod
    def get_record_join_folder(material_id):
        db = db_session()
        smtp = select(Material).options(joinedload(Material.folder)).where(Material.id == material_id)
        material_db = db.scalars(smtp).first()
        return material_db

    @staticmethod
    def get_all_records():
        db = db_session()
        smtp = select(Material)
        materials_db = db.scalars(smtp).all()
        return materials_db
