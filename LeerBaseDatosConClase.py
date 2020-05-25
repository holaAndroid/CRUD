import pymysql

from claseconnect import *

clasecon=Claseconnect()

clasecon.ejecutarSQL("SELECT * FROM employees")

data = clasecon.DevolverDatos()

for fila in data:
  Id = fila[0]
  Name = fila[1]
  Salary = fila[2]
#imprimir
print(data)

#desconecta
clasecon.CerrarBasededatos()
