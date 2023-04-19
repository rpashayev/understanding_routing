from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hi_name(name):
    return f'Hi {name.title()}!'

@app.route('/repeat/<int:n>/<string:str>')
def repeat(n, str):
    output = ''
    for i in range(n):
        output += '<h1>' + str + '</h1>' 
    return output

@app.errorhandler(404)
def error_code(err):
    return 'Sorry! No response. Try again'

if __name__=="__main__":
    app.run(debug=True)
    