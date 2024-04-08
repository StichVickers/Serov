from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,JSON
from db import Base

class Categorys(Base):
    __tablename__ = 'categorys'
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    name = Column(String,nullable=False,index=True)
    description = Column(String,nullable=False)
