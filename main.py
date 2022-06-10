from flask import Flask, render_template, request, redirect, send_from_directory, url_for, flash, session
from models.login import usuariosmodels
from models.login import archivo
from controller.login.inicio import ingreso
from controller.login.archivos import guardarimagenes
from controller.login.guard import registrarusuario
from controller.login.inicio import correo
from controller.login.guard import cambiapas
from controller.login.archivos import eliminar
from controller.acortador import acortardor
from controller.comprimir import rar
from models.acortador import acort
from models.zip import comprimir


app = Flask(__name__)
app.secret_key = "sdasdasdasd"


@app.get("/")
def login():
    if 'usuario_id' in session:
        archivos = archivo.obtenerarchivo(id=session["usuario_id"])
        return render_template("/archivos/archivos.html", archivos=archivos)

    return render_template("/validacion/login.html")


@app.post("/")
def ingresar():

    if ingreso.validaringreso(email=request.form.get('email'), password=request.form.get('password')):
        return render_template("/archivos/archivos.html", email=request.form.get('email'), password=request.form.get('password'))

    if 'usuario_id' in session:
        archivos = archivo.obtenerarchivo(id=session["usuario_id"])
        return render_template("/archivos/archivos.html", archivos=archivos)

    return render_template("/validacion/login.html", email=request.form.get('email'))


@app.get("/muestra")
def mostrar():
    return render_template("/validacion/inicio.html")


@app.get("/crear")
def crearUsuario():
    return render_template("/validacion/crear.html")


@app.post("/crear")
def crearUsuarioPost():
    if registrarusuario.registrar(nombre=request.form.get('nombre'), email=request.form.get('email'), password=request.form.get('password')):
        return render_template("/validacion/crear.html", nombre=request.form.get('nombre'), email=request.form.get('email'), password=request.form.get('password'))
    return render_template("/validacion/login.html")


@app.get("/añadir")
def guardarimagen():
    return render_template("/archivos/archivos.html", archivos=archivo.obtenerarchivo(id=session["usuario_id"]))


@app.post("/añadir")
def guardarimagenpost():
    guardarimagenes.guardar(nombre=request.form.get('nombre'), imagen=request.files['imagen'])
    return redirect(url_for('guardarimagen'))


@app.get("/limpiar")
def cerrarsesion():
    session.clear()
    return render_template("/validacion/login.html")


@app.route("/activar/<url>/<toke>")
def activar(url, toke):
    usuariosmodels.activar(url=url, toke=toke)
    return redirect(url_for("ingresar"))


@app.get("/recuperar")
def recuperarcontra():
    return render_template("/validacion/recuperar.html")


@app.post("/recuperar")
def recuperarcontrapost():
    if correo.sicorreo(direccion=request.form.get('email')):
        return render_template("/validacion/recuperar.html", direccion=request.form.get('email'))
    return render_template("/validacion/login.html")


@app.route("/restablecer/<toke>")
def contrapost(toke):
    if toke != None:
        return render_template("/validacion/restablecer.html", toke=toke)
    return render_template("/validacion/recuperarcontra")


@app.get("/contraupdates")
def contraup():
    return render_template("/validacion/restablecer.html")


@app.post("/contraupdates")
def contraupdate():
    if cambiapas.cambiarpass(password1=request.form.get('password1'), password=request.form.get('password'), toke=request.form.get('toke')):
        return render_template("/validacion/login.html")
    return render_template("/validacion/restablecer.html", password=request.form.get('password'), toke=request.form.get('toke'))


@app.post("/eliminar")
def eliminararchivo():
    archivos = eliminar.eliminararchivo(id=request.form.get('id'))
    return render_template("/archivos/archivos.html", archivos=archivos)


@app.get("/editar/<id>")
def editararchivo(id):
    return render_template("/editar/editar.html", archivo=archivo.editararchivo(id=id))


@app.post("/editar")
def editararchivopost():
    guardarimagenes.updateimagen(nombre=request.form.get('nombre'), imagen=request.files['imagen'], id=request.form.get('id'))
    return render_template("/archivos/verarchivos.html", archivos=archivo.obtenerarchivo(id=session["usuario_id"]))


@app.get("/ver/<id>")
def verarchivos(id):
    return render_template("/archivos/verarchivos.html", archivos=archivo.misarchvios(id=id))


@app.get("/descargas/<id>")
def descargar(id):
    archivos = archivo.misarchvios(id)
    filename = archivos[0]['img']
    return send_from_directory('./static/image/', path=archivos[0]['img'], as_attachment=True)


@app.get("/acortar")
def acortar():
    forms = acortardor.acortar()
    return render_template("/acortador/inicioacortador.html", forms=forms)


@app.post("/acortar")
def acortarPost():
    acort.gaurdaracortado()
    forms = acortardor.acortar()
    flash(forms[1], 'info')
    return render_template("/acortador/inicioacortador.html", forms=forms)


@app.route("/acortar/<url>")
def cortarRoute(url):
    acort.rutacorta(url)
    return redirect(url_for("acortar"))

@app.get("/zip")
def comprimi():
    return render_template("/zip/zip.html")

@app.post("/zip")
def comprimipost():
    rar.compress(ruta=request.form.get('nombre'),nombre=request.files.getlist('archivo[]'))
    return render_template("/zip/zip.html")

@app.route("/down")
def zipdes():
    ruta=comprimir.traer()
    return send_from_directory('./static/comprimido/', path=ruta, as_attachment=True)

@app.route("/files")
def zipdesc():
    ruta=request.args.get("ruta")
    return send_from_directory('./static/descomprimido/', path=ruta, as_attachment=True)

@app.get("/dezip")
def descomprimi():
    comprimir.vaciard()
    return render_template("/zip/deszip.html")

@app.post("/dezip")
def descomprimipost():
    archivos=rar.decompress(nombre=request.files['archivo'])
    return render_template("/zip/archi.html",archivos=archivos) 
 
#app.run(debug=True)
