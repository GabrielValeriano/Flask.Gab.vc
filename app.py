from flask import Flask

app = Flask(__name__)

@app.route("/necesito/papel")
def papel():
    return "<p>Me olvide el papel del baño Ayuda</p>"

@app.route("/necesito/salir")
def salir():
    return "<p>Me olvide la llave del baño Ayuda</p>"