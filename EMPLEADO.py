class EMPLEADO:
    def __init__(self, id_empleado, nombre, direccion):
        self.__id_empleado = id_empleado
        self.__nombre = nombre
        self.__direccion =direccion

    def guardar(self):
        f = open("c:\Programas\EMPLEADO.txt","a", encoding="utf8")
        f.write(str(self.__id_empleado)+'|')
        f.write(str(self.__nombre)+'|')
        f.write(str(self.__direccion)+ '\n')
        f.close()
