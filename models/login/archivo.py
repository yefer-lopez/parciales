from cgi import print_arguments
from email.mime import image
from requests import delete, session
from config.database import db
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

def obtenerarchivo(id):
  
    cursor= db.cursor(dictionary=True)
    cursor.execute("SELECT * from imagenes where id_imagen = %s ",(
        id,
    ))
    archivos = cursor.fetchall()   
    cursor.close()
    
    return archivos

def guardararchivos(idpersona,nombre, imagen,peso,extension,exten):
   
    cursor = db.cursor() 
    cursor.execute("INSERT into imagenes(nombre,img,id_imagen,peso,extension,exten) values (%s,%s,%s,%s,%s,%s)", (
        nombre,
        imagen,
        idpersona,
        peso,
        extension,
        exten
    ))
    cursor.close()    
    
def eliminararchivo(id):
    
    cursor= db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM imagenes WHERE id = %s ",(
        id,
    )) 
    archivo = cursor.fetchall() 
    cursor.close()
    
    cursor= db.cursor(dictionary=True)
    cursor.execute("DELETE FROM imagenes WHERE id = %s ",(
        id,
    )) 
    cursor.close()
    
    return
    
def editararchivo(id):
    
    cursor= db.cursor(dictionary=True)
    cursor.execute("SELECT * from imagenes where id = %s ",(
        id,
    ))
    archivos = cursor.fetchall()   
    cursor.close()
 
    return archivos

def guardararchivo(nombre, imagen,id,peso,extension,exten):
    
    if imagen == '':
        cursor = db.cursor()
        cursor.execute("UPDATE imagenes SET nombre= %s WHERE  id = (%s)", (
            nombre,
            id
        ))
        cursor.close()
     
    else:
        cursor = db.cursor() 
        cursor.execute("UPDATE imagenes SET nombre= %s , img= %s, peso=%s , extension=%s, exten=%s WHERE  id = (%s)", (
            nombre,
            imagen,
            peso,
            extension,
            exten,
            id
        ))
        cursor.close()  
    
   
def misarchvios(id):
    cursor= db.cursor(dictionary=True)
    cursor.execute("SELECT * from imagenes where id = %s ",(
        id,
    ))
    archivos = cursor.fetchall()   
    cursor.close()
    root,extension=os.path.splitext(archivos[0]['exten'])
 
    return archivos


    
