from flask import Flask

app = Flask(__name__)

@app.route('/<nome>') # Aqui eu defino que a URL vai ter uma parte variável chamada nome
def SayHello(nome): # passo nome como argumento na função
    return f"Olá, {nome} tudo bem com você? " # Retorno uma stringo com nome sendo passado dentro da f-string

if __name__ == '__main__':
    app.run(debug=True)