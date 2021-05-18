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
    x= int(input("¿Quieres seguir realizando acciones? (1 para seguir - *otro número* para salir): "))
    if x != 1:
        break



