from flask import Flask
from flask import Flask, url_for
import sqlite3

app = Flask(__name__)

def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}

def AbrirConexion():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = dict_factory

def CerrarConexion():
    global db 
    db.close()
    db = None

@app.route("/test/DB")
def testDB():
    AbrirConexion()
    cursor  = db.cursor()
    cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
    res = cursor.fetchone()
    registros = res["cant"]
    CerrarConexion()
    return f"Hay {registros} registros en la tabla usuarios"

@app.route("/")
def Principal():
    url_nota = url_for("notas", nombre = "Gabriel")
    url_Bpapel = url_for("papel")
    url_llave = url_for("salir")

    return F"""
    <a href="{url_nota}">nota</a>
    <br>
    <a href="{url_Bpapel}">papel</a>
    <br>
    <a href="{url_llave}">salir</a>
    """

@app.route("/crearUsuario/<string:nombre>/<string:email>")
def testCrear(nombre,email):
    AbrirConexion()
    cursor = db.cursor()
    consulta = "INSERT INTO usuarios(usuario, email) VALUES (?, ?);"
    cursor.execute(consulta, (nombre, email))
    db.commit()
    CerrarConexion()
    return f"Registro agregado ({nombre})"

@app.route("/crearUsuario/<string:nombre>/<string:email>")
def testCrear(nombre,email):
    AbrirConexion()
    cursor = db.cursor()
    consulta = "INSERT INTO usuarios(usuario, email) VALUES (?, ?);"
    cursor.execute(consulta, (nombre, email))
    db.commit()
    CerrarConexion()
    return f"Registro agregado ({nombre})"

@app.route("/crearUsuar")
def testCrearif():
    nombre = "Juan"
    email = "juan@etec.uba.ar"
    if nombre == "Juan":
        AbrirConexion()
        cursor = db.cursor()
        consulta = "INSERT INTO usuarios(usuario, email) VALUES (?, ?);"
        cursor.execute(consulta, (nombre, email))
        db.commit()
        CerrarConexion()  
        return f"Registro agregado ({nombre})"
    else:
        return "Ya esta agregado el usuario"


@app.route("/necesito/papel")
def papel():
    return """<p>Me olvide el papel del baño Ayuda</p>
    """

@app.route("/necesito/salir")
def salir():
    return "<p>Me olvide la llave del baño Ayuda</p>"

@app.route("/nota/DiseñoDeSoftware/<string:nombr>")
def notas(nombre):
    n = nombre
    if nombre == "Gabriel":
        return f"<p>La nota de {n}: 10</p>"
    if nombre == "Sol":
        return f"<p>La nota de {n}: 7</p>"
    if nombre == "Briseida":
        return f"<p>La nota de {n}: 7</p>"
    if nombre == "Miguel":
        return f"<p>La nota de {n}: 9</p>"
    if nombre == "Joel":
        return f"<p>La nota de {n}: 7</p>"
    