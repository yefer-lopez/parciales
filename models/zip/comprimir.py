from config.database import db
from flask import render_template, flash,session

def compresszip(nombre,ruta,exten,ubicacion):
    cursor = db.cursor()
    cursor.execute("INSERT INTO zip(nombre,ruta,final,ubicacion) VALUES (%s,%s,%s,%s)", (
        nombre,
        ruta,
        exten,
        ubicacion,
    ))
    cursor.close()
    
def verzip():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM  zip ")
    forms = cursor.fetchone()
    cursor.close() 

    return forms

def vaciar():
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE zip")
    cursor.close() 

def vaciard():
    cursor = db.cursor()
    cursor.execute(" TRUNCATE TABLE deszip")
    cursor.close() 
    
def traer():
    cursor = db.cursor()
    cursor.execute("SELECT nombre,final FROM zip")
    url = cursor.fetchone()
    ruta=url[0]+url[1]
    return ruta

def anadirarchivo(nombre,ruta,extencion,exten,img):
    cursor = db.cursor()
    cursor.execute("INSERT INTO deszip(nombre,ruta,extencion,exten,img) VALUES (%s,%s,%s,%s,%s)", (
        nombre,
        ruta,
        extencion,
        exten,
        img,
    ))
    cursor.close()

def misarchivos():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM  deszip ")
    archivos= cursor.fetchall()
    cursor.close() 
    
    return archivos

