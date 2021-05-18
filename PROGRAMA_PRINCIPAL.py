from TEMA import TEMA
from CURSO import CURSO
from VIDEO import VIDEO
from EMPLEADO import EMPLEADO
from CURSO_TEMA import CURSO_TEMA
from CURSO_TEMA_VIDEO import CURSO_TEMA_VIDEO

x=1
while True:
    print ("**MENU DE ADMINISTRADOR**")
    des = int(input("\nElige la base de datos a trabajar.\n1-TEMA. 2-CURSO. 3-VIDEO. 4-EMPLEADO. 5-CURSO_TEMA. 6-CURSO_TEMA_VIDEO. : "))
    opc = int(input("\nElige la acción que quieres realizar.\n1-Insertar datos. 2-Revisar todos los datos. 3.Consultar datos por ID: "))
    if des == 1:
        if opc == 1:
            a = input("Escribe el id del tema: ")
            b = input("Escribe el nombre del tema: ")
            info = TEMA(a,b)
            info.guardar()
        elif opc == 2:
            print("ID_TEMA | NOMBRE")
            TEMA.consultar_todo()
        elif opc == 3:
            TEMA.consultar_por_id()
    elif des == 2:
        if opc == 1:
            a = input("Escribe el id del curso: ")
            b = input("Escribe la descripcion del curso: ")
            c = input("Escribe el id del empleado que lo imparte: ")
            info = CURSO(a,b,c)
            info.guardar()
        
        elif opc == 2:
            print("ID_CURSO | DESCRIPCION | ID_EMPLEADO")
            CURSO.consultar_todo()
        elif opc == 3:
            CURSO.consultar_por_id()
    
    elif des == 3:
        if opc == 1:
            a = input("Escribe el id del video: ")
            b = input("Escribe el nombre del video: ")
            c = input("Escribe el url del video: ")
            d = input("Escribe la fecha de publicación: ")
            info = VIDEO(a,b,c,d)
            info.guardar()
        elif opc == 2:
            print("ID_VIDEO | NOMBRE | URL | FECHA")
            VIDEO.consultar_todo()
        elif opc == 3:
            VIDEO.consultar_por_id()
    elif des == 4:
        if opc == 1:
            a = input("Escribe el id del empleado: ")
            b = input("Escribe el nombre del empleado: ")
            c = input("Escribe la dirección del empleado: ")
            info = EMPLEADO(a,b,c)
            info.guardar()
        if opc == 2:
            print("ID_EMPLEADO | NOMBRE | DIRECCIÓN")
            EMPLEADO.consultar_todo()
        if opc == 3:
            EMPLEADO.consultar_por_id()
    x= int(input("¿Quieres seguir realizando acciones? (1 para seguir - *otro número* para salir): "))
    if x != 1:
        break



