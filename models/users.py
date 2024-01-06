from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime



class User(Base):
    
    __tablename__="User"
    
    id = Column(Integer, primary_key= True, autoincrement=True)
    nombre = Column(String)
    cedula = Column(Integer)
    password = Column(String)
    correo = Column(String)
    rol = Column(String)
      