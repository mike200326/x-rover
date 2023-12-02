# import mysql.connector
# from temperatura import Temperatura
# from fastapi import FastAPI
# import mysql.connector
from temperatura import Temperatura
# from fastapi.middleware.cors import CORSMiddleware
from temperatura import Presion
from temperatura import Distancia

import mysql.connector

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from time import sleep
import time
from datetime import datetime

app = FastAPI()
origins = [
       "http://localhost:3000",
       "https://frontend-dot-top-sunrise-406620.uc.r.appspot.com/"
       
]
# Conexión a la base de datos

mydb = mysql.connector.connect(
    host="35.192.27.233",
    user="root",
    password="equipo_4",
    database="CARRO"
)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/temperaturas")

async def root():
    temperaturas=[]
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Temperatura")
    temperaturas_db = mycursor.fetchall()
    mydb.commit()
    for temperatura in temperaturas_db:
        t=Temperatura(temperatura[0],temperatura[1],temperatura[2])
        temperaturas.append(t)
    return temperaturas

# RUTA PARA OBTENER PRESION
@app.get("/presion")
async def get_presion():
    presiones = []
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Presion")
    presiones_db = mycursor.fetchall()
    mydb.commit()
    for presion in presiones_db:
        p = Presion(presion[0], presion[1], presion[2])
        presiones.append(p)
    return presiones

# RUTA PARA OBTENER DISTANCIA
@app.get("/distancia")
async def get_distancia():
    distancias = []
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Distancia")
    distancias_db = mycursor.fetchall()
    mydb.commit()
    for distancia in distancias_db:
        d = Distancia(distancia[0], distancia[1], fecha=distancia[2])
        distancias.append(d)
    return distancias


def insert_temperatura(temperatura):
    mycursor = mydb.cursor()
    sql = "INSERT INTO Temperatura (temperatura) VALUES (%s)"
    val = (temperatura,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def find_temperaturas():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Temperatura")
    temperaturas_db = mycursor.fetchall()
    for temperatura in temperaturas_db:
        t=Temperatura(temperatura[0],temperatura[1],temperatura[2])
        print(t.temperatura)
