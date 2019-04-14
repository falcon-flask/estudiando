from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo, cambio'

@app.route('/saluda')
def saluda():
    return 'otro mensaje'

# http://127.0.0.1:8000/params?params1=marlon
# http://127.0.0.1:8000/params?params1=marlon&params2=juan

@app.route('/params')
def params():
    param = request.args.get('params1','no contiene')
    param2 = request.args.get('params2','no contiene')
    return 'El parametro es {}, {}'.format(param,param2) 

if __name__ == '__main__':
    app.run(debug = True, port=8000)
