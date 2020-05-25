import pymysql
from claseconnect import *

#Llamamos al constructor
clasecon = Claseconnect()

#Pedir a el usuario un  dato
Name = input("introduce un nombre: ")
Salary = input("introduce un salario: ")
#id=(input("introduce una id:")
#Ejecutar sql
clasecon.ejecutarSQL("INSERT INTO employees (Name, Salary) VALUES('"+Name+"',"+Salary+")")
clasecon.RealizarCambio()
#clasecon.ejecutarSQL("SELECT * FROM employees WHERE Name='"+nombre+"'")
#clasecon.ejecutarSQL("SELECT * FROM employees WHERE Name='Francisco'")
#clasecon.ejecutarSQL("SELECT * FROM employees WHERE Id="+Id)

datos = clasecon.DevolverDatos()
#recorrer tabla
  #print("Id=%i, Nombre=%s, Salario=%s" % (Id, Name, Salary))
print(datos)
#cerramos

clasecon.CerrarBasededatos()
