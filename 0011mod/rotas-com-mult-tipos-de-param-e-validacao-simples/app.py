from flask import Flask

app = Flask(__name__)

@app.route("/")
def SayHelloDefault():
    return "Olá mundo no Flask"

@app.route("/<int:numero>")
def SayMultiple(numero):
    return f"O dobro de {numero} é {2 * numero}."

if __name__ == "__main__":
    app.run(debug=True)