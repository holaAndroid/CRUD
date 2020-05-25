import pymysql

from claseconnect import *
#Conexión al servidor.
db=Claseconnect()

Clave=input("Introduce clave principal ")
#hacemos la consulta
sqlconsulta ="SELECT * FROM employees WHERE Id="+Clave

db.ejecutarSQL(sqlconsulta)

resultado=db.DevolverDatos()

if len(resultado) > 0:
    print(resultado)
    Name=input("Introduce un nombre")
    Salary=input("Introduce tu salario") 
    sql="UPDATE EMPLOYEES set Name='"+Name+"',Salary="+Salary+" WHERE id="+Clave
    try:
        db.ejecutarSQL(sql)
        db.RealizarCambio()
        print("Realizado el cambio")
        db.ejecutarSQL(sqlconsulta)
        resultado=db.DevolverDatos()
        print(resultado)

    except:
        db.NoRealizarCambio()
        print("No se puede realizar el cambio")
else:
    print("Registro no encontrado")

db.CerrarBasededatos()
