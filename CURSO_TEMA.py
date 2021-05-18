class CURSO_TEMA:
    def __init__(self, id_CT, id_curso, id_tema):
        self.__id_CT = id_CT
        self.__id_curso = id_curso
        self.__id_tema = id_tema

    def guardar(self):
        f = open("c:\Programas\CURSO_TEMA.txt","a", encoding="utf8")
        f.write(str(self.__id_CT)+'|')
        f.write(str(self.__id_curso)+'|')
        f.write(str(self.__id_tema)+ '\n')
        f.close()

    @classmethod
    def consultar_todo(cls):
        f = open("c:\Programas\CURSO_TEMA.txt")
        print(f.read())
        f.close()

    @classmethod
    def consultar_por_id(cls):
        busqueda = input("**Consulta datos por id** Inserte id a consultar:")
        f = open("c:\Programas\CURSO_TEMA.txt")
        for linea in f:
            info = linea.strip().split('|')
            if info[0] == busqueda:
                print(linea)
        f.close()