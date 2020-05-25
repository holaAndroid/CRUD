import pymysql
from claseconnect import *

#Llamamos al constructor
clasecon=Claseconnect()

#Pedir a el usuario un  dato
nombre=input("introduce un nombre: ")
#id=(input("introduce una id:")
#Ejecutar sql
#clasecon.ejecutarSQL("SELECT * FROM employees WHERE Name='"+nombre+"'")
#clasecon.ejecutarSQL("SELECT * FROM employees WHERE Name='Francisco'")
#clasecon.ejecutarSQL("SELECT * FROM employees WHERE Id="+Id)

#damo datos
clasecon.ejecutarSQL("SELECT * FROM employees WHERE Name='"+nombre+"'")
datos=clasecon.DevolverDatos()
#recorrer tabla
for fila in datos:
  Id = fila[0]
  Name = fila[1]
  Salary = fila[2]
  print ("Id=%i, Nombre=%s, Salario=%s" %(Id,Name, Salary))

#cerramos
  clasecon.CerrarBasededatos

