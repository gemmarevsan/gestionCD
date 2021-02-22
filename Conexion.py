import mysql.connector

class Conexion:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='´musica´') #abrir conexion a la bd
        self.cursor = self.cnx.cursor()