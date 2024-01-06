from fastapi import FastAPI, Request,Response,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from config.database import Session, engine, Base
from models.users import User as UserModel
from pydantic import BaseModel, Field
from typing import Optional
#from schemas.schemas import User as UserModel

app = FastAPI()
app.title = "FOTOREPORTE"
app.version = "0.0.1"

def create_tables():
    Base.metadata.create_all(bind=engine)
    
create_tables()
    


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", "r") as file:
        return file.read()

@app.get("/createUser", response_class=HTMLResponse)
async def formCreateUser():
    with open("templates/createUser.html", "r") as file:
        return file.read()
    
#recibiendo datos para crear usuario
@app.post("/create", response_class=HTMLResponse)
def create(username:str = Form(), cedula:int = Form(),password:str = Form(),mail:str =Form(),rol:str = Form()):
    new_user_data = {
    "nombre": username,
    "cedula": cedula,
    "password":password,
    "correo": mail,
    "rol":rol
      
    }
    new_user = UserModel(**new_user_data)
    db = Session()
    db.add(new_user)
    db.commit()
    print(new_user)
    return("save user")
    
@app.get("/login", response_class=HTMLResponse)
async def mostrar_formulario():
    with open("templates/login.html", "r") as file:
        return file.read()

@app.post("/login", response_class=HTMLResponse)
async def procesar_formulario(nombre: str, password: str):
    datos = {"nombre": nombre, "password": password}
    print(datos)
    # Realiza aquí cualquier procesamiento adicional que necesites.

    
@app.get("/crear-reporte", response_class=HTMLResponse)
async def read_root():
    with open("templates/crearp.html", "r") as file:
        return file.read()

@app.get("/hallazgo", response_class=HTMLResponse)
async def read_root():
    with open("templates/hallazgo.html", "r") as file:
        return file.read()