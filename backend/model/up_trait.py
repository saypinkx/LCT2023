from model.user import Base
from sqlalchemy import ForeignKey, Table, Column, Integer

up_trait = Table('lc_up_traits',
                 Base.metadata,
                 Column('id', Integer, primary_key=True),
                 Column('up_id', Integer, ForeignKey('lc_user_profiles.id')),
                 Column('trait_id', Integer, ForeignKey('lc_traits.id'))
                 )
