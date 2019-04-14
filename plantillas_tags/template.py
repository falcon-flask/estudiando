from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name='Marlon'):
    age = 17
    mylist = [1,2,3,4]
    return render_template('index.html', nombre=name, age=age, list=mylist)

if __name__ == '__main__':
    app.run(debug = True, port=8000)
