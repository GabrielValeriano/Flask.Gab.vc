from flask import Flask
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def Principal():
    url_nota = url_for("notas")
    url_Bpapel = url_for("papel")
    url_llave = url_for("salir")

    return """
    <a href="{url_nota}">nota</a>
    <br>
    <a href="{url_Bpapel}">papel</a>
    <br>
    <a href="{url_llave}">salir</a>
    """

@app.route("/necesito/papel")
def papel():
    return """<p>Me olvide el papel del baño Ayuda</p>
    <br>
    <a href=">necesito/papel">papel</a>
    <a href=">papel">papel 2</a>
    """

@app.route("/necesito/salir")
def salir():
    return "<p>Me olvide la llave del baño Ayuda</p>"

@app.route("/nota/DiseñoDeSoftware/<string:nombre>")
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
    