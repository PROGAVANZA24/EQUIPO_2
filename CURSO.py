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