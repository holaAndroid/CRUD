from flask import Flask, jsonify, render_template, request, redirect
from claseconnect import *
import pymysql

app=Flask(__name__)

@app.route("/")
def presentation():
    return render_template("home.html")

@app.route("/<name>")
def saludo(name):
    return "hola Don/Doña"+str(name)

@app.route('/add',methods=["POST"])
def insertar():
        #name=request.form.get("nombre")
        #salary=request.form.get("salary")
        #cone = Claseconnect()
        #cone.ejecutarSQL("INSERT INTO employees(name,salary) VALUES('"+name+"',"+salary+")")
        #cone.RealizarCambio()
    try:
        name = request.form.get("name")
        salary = request.form.get("salary")
        cone = Claseconnect()
        print(name)
        print(salary)
        cone.ejecutarSQL("INSERT INTO employees(name,salary) VALUES('"+name+"',"+salary+")")
        cone.RealizarCambio()
    except Exception:
        cone.NoRealizarCambio()
        print("error en las altas")
    return redirect("/all")


@app.route("/update",methods=["POST"])
def update():
    id=request.form.get("id")
    Name=request.form.get("nombre")
    salary=request.form.get("salary")
    conectar=Claseconnect()
    conectar.ejecutarSQL("UPDATE employees SET Name='"+Name+"',Salary="+salary+" WHERE id="+id)
    conectar.RealizarCambio()
    return redirect("all")

@app.route("/delete",methods=["POST"])
def delete():
    try:
        id=request.form.get('id')
        cone = Claseconnect()
        cone.ejecutarSQL("DELETE FROM employees WHERE id="+id)
        cone.RealizarCambio()
    except Exception:
        cone.NoRealizarCambio()
        print("error en las bajas")
    return redirect("/all")

@app.route("/list")
def listado_alumno():
    cone=Claseconnect()
    cone.ejecutarSQL("SELECT * FROM employees")
    datos=cone.DevolverDatos()
    resp=jsonify(datos)
    cone.CerrarBasededatos()
    return resp


@app.route("/view")
def listView():
    cone = Claseconnect()
    cone.ejecutarSQL("SELECT * FROM employees")
    datos = cone.DevolverDatos()
    resp = jsonify(datos)
    cone.CerrarBasededatos()
    return render_template("listado.html", datos=datos)


@app.route("/all")
def listall():
    cone = Claseconnect()
    cone.ejecutarSQL("SELECT * FROM employees")
    datos = cone.DevolverDatos()
    cone.CerrarBasededatos()
    return render_template("index.html",datos=datos)

if __name__=="__main__":
    app.run(debug=True,port=8000)
    #app.run()

