from flask import Flask

app  = Flask(__name__)

@app.route('/')
def SayHello():
    return "Olá, Mundo com Flask"

if __name__ == '__main__':
    app.run(debug=True)