import pymysql

class Claseconnect():
    def __init__(self):
        #Conectarme con la base de datos
        self.CrearConnect()
        #Abrir la conexión
        self.AbrirConnect()
    def CrearConnect(self):
        self.db = pymysql.connect(
            host="localhost",
            port=3306, user="root",
            passwd="holaAndroid10",
            db="company"
        )
    def AbrirConnect(self):
        self.cursor = self.db.cursor()
    
    def ejecutarSQL(self,sql):
        self.cursor.execute(sql)
    
    def DevolverDatos(self):
        return self.cursor.fetchall()
    
    def CerrarBasededatos(self):
        self.db.close()

    def RealizarCambio(self):
        self.db.commit()
    
    def NoRealizarCambio(self):
        self.db.rollback()
    
