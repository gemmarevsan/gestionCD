from Idioma import Idioma
import mysql.connector
# from Conexion import Conexion

class AdminIdioma:
    def __init__(self):

    # def conexion1(self):
    #     Conexion.conexion()

        self.cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='´musica´') #abrir conexion a la bd
        self.cursor = self.cnx.cursor()
        
    def create(self,idioma):
        insert="insert into idioma (nombre) values('%s')"% (idioma.getNombre())
        self.cursor.execute(insert)
        self.cnx.commit()
        self.cursor.close()

    def read(self,idioma):
        query = 'SELECT * FROM idioma'
        self.cursor.execute(query)
        self.cnx.commit()
        self.cursor.close()





