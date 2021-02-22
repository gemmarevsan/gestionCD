from Idioma import Idioma
from AdminIdioma import AdminIdioma

cerrarConexcion=False

while not cerrarConexcion:
    print('\n1.Ver idiomas \n2.Añadir idiomas \n3.Modificar idiomas \n4.Borrar idiomas \n5.Cerrar conexión ')

    option=int(input('\nIntroduce la opción deseada:'))

    if option==1:
        pass
    elif option==2:
        nombreIdioma=input('Indica el idioma para añadir: ') 
        idioma=Idioma('',nombreIdioma)
        adminIdioma=AdminIdioma()
        adminIdioma.create(idioma)
        print(nombreIdioma+' añadido a la base de datos')
    elif option==3:
        pass
    elif option==4:
        pass
    elif option==5:
        pass
    else:
        print('Comando incorrecto')







