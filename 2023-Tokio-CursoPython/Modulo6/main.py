#Importamos flask para configurar el servidor web
from flask import Flask

#Delcaramos la aplicación web con Flask
app = Flask(__name__)


#Creamos la página principal (home), que se econtrará en la ruta '/' y al entrar devuelve un texto.
@app.route('/')
def home():
    return "Página principal. RAA"


@app.route('/raa/')
def second():
    return "Página secundaria. RAA"

if __name__ == '__main__':
    #Arrancamos el servidor web. Al utilizar debug = True, cada vez que se reinnice el servidor o se modifique
    #el código, el servidor se reiniciará solo.
    app.run(debug = True)
    