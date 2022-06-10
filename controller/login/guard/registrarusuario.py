
from flask import Flask, render_template, request, redirect, url_for, flash, session
from controller.login.inicio import validarcorreo
from models.login import usuariosmodels
from controller.login.inicio import send_main
from controller.login.inicio import token
from models.login import cargarpas

def registrar(nombre,email,password):
    
    valido1 = validarcorreo.validarlog(nombre=nombre,email=email)
    correo = validarcorreo.validarpas(password=password)
    valido = validarcorreo.correovalido(email=email)
    usuario = usuariosmodels.verificarusuario(email=email)
    valor=validarcorreo.redir(usuario=usuario,valido1=valido1,valido=valido,correo=correo)
    
    if valor == True:
        return render_template("crear.html", nombre=nombre, email=email, password=password)
    else:
        usuariosmodels.crearusuario(nombre=nombre, email=email, password=password)
        direccion = email
        valor = 1
        toke = token.acortarPost()
        cargarpas.cargartokenpassword(direccion=email,toke=toke)
        send_main.correo(direccion=direccion,valor=valor,toke=toke) 
    
    return