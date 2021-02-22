class Idioma:
    def __init__(self,ididioma,nombre):
        self.__ididioma=ididioma
        self.__nombre=nombre

    def getIdidioma(self):
        return self.__ididioma
    def setIdidioma(self,ididioma):
        self.__ididioma=ididioma

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    def __str__(self):
        return "Id: "+str(self.__ididioma)+" Nombre:"+str(self.__nombre)