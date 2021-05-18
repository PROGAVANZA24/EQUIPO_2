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

    def consultar_todo(self):
        f = open("c:\Programas\CURSO_TEMA.txt")
        print(f.read())
        f.close()