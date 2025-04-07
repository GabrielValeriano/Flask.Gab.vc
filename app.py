from flask import Flask

app = Flask(__name__)

@app.route("/necesito/papel")
def papel():
    return "<p>Me olvide el papel del baño Ayuda</p>"

@app.route("/necesito/salir")
def salir():
    return """
    <p>Me olvide la llave del baño Ayuda</p>
    <a href="/static/PRUEBA.html">pagina</a>
    """

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
    