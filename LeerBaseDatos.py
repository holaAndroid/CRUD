import pymysql

#Conexion a la base de datos
db = pymysql.connect(
    host="localhost", 
    port=3306, user="root",
    db="company"
)
# puntero a la conexión
cursor = db.cursor() #abriendo la bd db
#sql
#'''sql = "SELECT * FROM employees
#WHERE id=1'''

#sql="Select * from employees"

#Ejecutar la sql
cursor.execute("SELECT * FROM employees")

# Fetchall te devuelve todas las filas.
#results = cursor.fetchall()
data =cursor.fetchall()

for fila in data:
  Id = fila [0]
  Name = fila [1]
  Salary = fila [2]
#imprimir
print(data)

#desconecta
db.close()
