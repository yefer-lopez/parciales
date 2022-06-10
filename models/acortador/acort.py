from controller.acortador import acortardor
from config.database import db
from flask import Flask, render_template, request, redirect, url_for, flash,session
import string
import random

def acortarlink():
    
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM  urls ORDER BY id DESC")
    forms = cursor.fetchone()
    
    if forms != None:
        return forms
    else:
        forms==None
        return forms
    

def gaurdaracortado():
    puerto = request.form.get('nurl')
    for x in range(5):
        code= (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)))
        
    forma = request.host_url+code
    cursor = db.cursor()
    cursor.execute("INSERT INTO urls(puerto,forma) VALUES (%s,%s)", (
        puerto,
        forma
    ))
    cursor.close()
    return

def rutacorta(url):
    url = request.host_url+url
    cursor = db.cursor()
    cursor.execute("SELECT puerto FROM urls WHERE forma = %s",(url,))
    url = cursor.fetchone()
    if(url != None): return redirect(url[0])
    return