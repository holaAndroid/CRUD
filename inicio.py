from flask import Flask,request, jsonify

app = Flask(__name__)
@app.route("/")
def Hello():
    return "Hola Don Pepito!"

@app.route("/Saludo")
def saludo():
    return "Soy Pepe Gotera"

@app.route("/edit")
def responder():
    return "Hola Yudith"

if __name__=="__main__":
        app.run()