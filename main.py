from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse




app = FastAPI()
app.title = "FOTOREPORTE"
app.version = "0.0.1"


locations = [
    {
     "id": 1,
     "name": "Ubication1",
     "address": "Direccion1",
     "positionlat": 4.8300,
     "positionlog": -75.6992,
     "state": "Cerrado"
    },
       {
     "id": 2,
     "name": "Ubication2",
     "address": "Direccion2",
     "positionlat": 4.8018,
     "positionlog": -75.7370,
     "state": "Pendiente"
    },
        {
     "id": 3,
     "name": "Ubication3",
     "address": "Direccion3",
     "positionlat": 4.83814,
     "positionlog": -75.66893,
     "state": "Cerrado"
    },
        {
     "id": 4,
     "name": "Ubication4",
     "address": "Direccion4",
     "positionlat": 4.81359,
     "positionlog": -75.71028,
     "state": "Pendiente"
    }
]
# def create_tables():
#     Base.metadata.create_all(bind=engine)
    
# create_tables()
    
@app.get('/', tags=['Home'])
def message():
    return "Hello World"


@app.get('/locations', tags=['Locations'])
def Locations():
    return locations

@app.get('/locations/{id}',tags=['Locations'])
def get_locations(id: int):
    for item in locations:
        if item["id"] == id:
            return item
    return []

@app.get('/locations/', tags=['Locations'])
def get_locations_name(name: str):
    for item in locations:
        if item["name"] == name:
            return item
    return []

@app.post('/locations', tags=['Locations'])
def create_location(id:int = Body(), name:str = Body(), address:str = Body(), positionlat:float = Body(), positionlog: float = Body(), state: str = Body()):
    locations.append({
    "id": id,
    "name": name,
    "address": address,
    "positionlat": positionlat,
    "positionlog": positionlog,
    "state": state
    })
    return locations
 
# app.mount("/static", StaticFiles(directory="static"), name="static")


# @app.get("/", response_class=HTMLResponse)
# async def read_root():
#     with open("templates/index.html", "r") as file:
#         return file.read()

# @app.get("/createUser", response_class=HTMLResponse)
# async def formCreateUser():
#     with open("templates/createUser.html", "r") as file:
#         return file.read()
    
# #recibiendo datos para crear usuario
# @app.post("/create", response_class=HTMLResponse)
# def create(username:str = Form(), cedula:int = Form(),password:str = Form(),mail:str =Form(),rol:str = Form()):
#     new_user_data = {
#     "nombre": username,
#     "cedula": cedula,
#     "password":password,
#     "correo": mail,
#     "rol":rol
      
#     }
#     new_user = UserModel(**new_user_data)
#     db = Session()
#     db.add(new_user)
#     db.commit()
#     print(new_user)
#     return("save user")
    
# @app.get("/login", response_class=HTMLResponse)
# async def mostrar_formulario():
#     with open("templates/login.html", "r") as file:
#         return file.read()

# @app.post("/login", response_class=HTMLResponse)
# async def procesar_formulario(nombre: str, password: str):
#     datos = {"nombre": nombre, "password": password}
#     print(datos)
#     # Realiza aquí cualquier procesamiento adicional que necesites.

    
# @app.get("/crear-reporte", response_class=HTMLResponse)
# async def read_root():
#     with open("templates/crearp.html", "r") as file:
#         return file.read()

# @app.get("/hallazgo", response_class=HTMLResponse)
# async def read_root():
#     with open("templates/hallazgo.html", "r") as file:
#         return file.read()