from ast import Str
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models.login import archivo
import os

def guardar(nombre,imagen):
    
    if nombre == "":
        flash("el nomre es obligatorio")  
        return render_template("inicio.html", nombre=nombre)
        
    idpersona = session["usuario_id"]
    imagen.save('./static/image/'+ imagen.filename)
    filename = ('./static/image/'+ imagen.filename)
    
    path = filename
    root, extension = os.path.splitext(path)
    exten=('../static/image/exten/'+str(extension)+'.jpg')
    peso=os.path.getsize(filename)
    peso = str(peso*0.000001) + " MB"
    
    
    archivo.guardararchivos(idpersona=idpersona, nombre=nombre, imagen='/static/image/'+ imagen.filename,peso=peso,extension=extension,exten=exten)
    return 

def updateimagen(nombre,imagen,id):
    
    if imagen.filename == '':
        ruta=imagen.filename
        peso=''
        extension=''
        exten=''
        
    else:
        
        imagen.save('./static/image/'+ imagen.filename)
        filename = ('./static/image/'+ imagen.filename)
        ruta=('/static/image/'+ imagen.filename)
        path = filename
        root, extension = os.path.splitext(path)
        exten=('../static/image/exten/'+str(extension)+'.jpg')
        peso=os.path.getsize(filename)
        peso = str(peso*0.000001) + "MB"
        
    archivo.guardararchivo(nombre=nombre, imagen=ruta,id=id,peso=peso,extension=extension,exten=exten)
    
    return
