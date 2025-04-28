# Flask.Gab.vc

## Entorno Virtual

Para crear el entorno virtual:

```
python -m venv .venv
```

Para activar el entorno virtual:

```
source .venv/bin/activate
```

Instalacion del paquete de requerimientos:
  
```
pip install flask
```

## Para correr el programa

Solo en la maquina local:

```
flask run
```

Te reinicia automaticamente la pagina al correrlo:

```
flask run --debug
```

Desde cualquier maquina de red:

```
flask run -h 0.0.0.0
```

Desde otra maquina, te reinicia automaticamente la pagina:

```
flask run -h 0.0.0.0 --debug
```