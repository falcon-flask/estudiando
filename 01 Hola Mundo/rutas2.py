from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo, cambio'

@app.route('/saluda')
def saluda():
    return 'otro mensaje'

# http://127.0.0.1:8000/params/marlon/


@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name = 'valor por default', num = 1):
    return 'El parametro es {} {}'.format(name, num) 

if __name__ == '__main__':
    app.run(debug = True, port=8000)
