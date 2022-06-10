
from importlib.resources import path
from msilib.schema import File
from ssl import AlertDescription
from statistics import mode
from trace import Trace
from unicodedata import name
from zipfile import ZipFile
import os
from shutil import rmtree, which
import shutil
import zipfile
from flask import Flask, render_template, request, redirect, send_from_directory, url_for, flash, session
from models.zip import comprimir

def compress(ruta,nombre):
    rmtree('./static/comprimido') 
    os.mkdir(('./static/comprimido'))
    comprimir.vaciar()
    
    if nombre[0].filename == '':
        flash("Debes seleccionar algun documento", 'danger')
        return render_template("/zip/zip.html")
    else: 
        
        if ruta == '':
            ruta = 'X'
        os.mkdir(('./static/image/'+ruta))
        num=int(len(nombre))
        for i in range(0, num):
            nombre[i].save('./static/image/'+ruta+'/'+ nombre[i].filename)
        
        exten=shutil.make_archive('./static/comprimido/'+ruta, "zip", './static/image/'+ruta)
        rmtree('./static/image/'+ruta) 
        root, extension = os.path.splitext(exten)
        comprimir.compresszip(nombre=ruta,ruta='./static/image/'+ruta,exten=extension,ubicacion='../static/image/exten/'+extension+".jpg")
        forms = comprimir.verzip()
        flash(forms[4], 'info')
    
def decompress(nombre):
    rmtree('./static/descomprimido')
    os.mkdir('./static/descomprimido')
    
    if nombre.filename == '':
        flash("Debes seleccionar algun documento", 'danger')
        return render_template("/zip/zip.html")
    else:
        root, extension = os.path.splitext(nombre.filename)
        archive_format = ['.rar','.zip','.RAR', '.ZIP', '.CAB', '.ARJ', '.LZH', '.TAR', '.GZ', '.ACE', '.UUE', '.BZ2', '.JAR', '.ISO', '.Z' , '.7Z']
        
        num=int(len(archive_format))
        for i in range(0, num):
            if extension == archive_format[i]:
                os.mkdir('./static/image/desc')
                nombre.save('./static/image/desc/'+root+'.zip')
                archivo=('./static/image/desc/'+root+'.zip')
    
                shutil.unpack_archive('./static/image/desc/'+root+'.zip','./static/descomprimido/',"zip") 
                rmtree('./static/image/desc')
                
                archivor=os.getcwd()
                archivo1=archivor +"\static\descomprimido"
                lugar=os.listdir(archivo1)
                narchivos=int(len(lugar))
                print("mis archivos")
                for i in range(0, narchivos):
                    root, extension = os.path.splitext(lugar[i])
                    exten="../static/image/exten/"+extension+".jpg"
                    img="/static/descomprimido/"+lugar[i]
                    comprimir.anadirarchivo(lugar[i],root,extension,exten,img)
                    archivos=comprimir.misarchivos()
                    
                return archivos
                #archivos=comprimir.misarchivos()
                #return render_template("/zip/archi.html",archivos)
            else:
                a=2
        
        if a==2:
            flash("El fomrato del archivo no es valido", 'danger')
            return render_template("/zip/deszip.html")       
        
        
        
        #forms = comprimir.verzip()
        
        
