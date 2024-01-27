from typing import Optional
from datetime import datetime
from pydantic import BaseModel

#user model
class User(BaseModel): #Schema
    id = int
    nombre = str
    cedula = int
    password = str
    correo = str
    rol = str