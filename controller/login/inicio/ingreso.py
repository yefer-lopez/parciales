from ast import Return
from flask import Flask, render_template, request, redirect, url_for, flash, session
from email.mime import image
from requests import session
from config.database import db
from models.login import usuariosmodels


def validaringreso(email, password):
    if email == "":
        flash("este campo es obligatorio")
    if password == "":
        flash("este campo es obligatorio")
        
    usuariosmodels.ingresoUsuario(email=email, password=password)
    
    return 