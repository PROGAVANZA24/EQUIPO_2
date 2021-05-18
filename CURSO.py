class CURSO:
    def __init__(self, id_curso, descripcion, id_empleado):
        self.__id_curso = id_curso
        self.__descripcion = descripcion
        self.__id_empleado = id_empleado

    def guardar(self):
        f = open("c:\Programas\CURSO.txt","a", encoding="utf8")
        f.write(str(self.__id_curso)+'|')
        f.write(str(self.__descripcion)+'|')
        f.write(str(self.__id_empleado)+ '\n')
        f.close()

    def consultar_todo(self):
        f = open("c:\Programas\CURSO.txt")
        print(f.read())
        f.close()

    @classmethod
    def consultar_por_id(cls):
        busqueda = input("**Consulta datos por id** Inserte id a consultar:")
        f = open("c:\Programas\CURSO.txt")
        for linea in f:
            info = linea.strip().split('|')
            if info[0] == busqueda:
                print(linea)
        f.close()