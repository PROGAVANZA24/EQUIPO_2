from os import write
class TEMA:
    def __init__(self, id_tema, nombre):
        self.__id_tema = id_tema
        self.__nombre = nombre

    def guardar(self):
        f = open("c:\Programas\TEMA.txt","a", encoding="utf8")
        f.write(str(self.__id_tema)+'|')
        f.write(str(self.__nombre)+'\n')
        f.close()

    @classmethod
    def consultar_todo(cls):
        f = open("c:\Programas\TEMA.txt")
        print(f.read())
        f.close()

    @classmethod
    def consultar_por_id(cls):
        busqueda = input("**Consulta datos por id** Inserte id a consultar:")
        f = open("c:\Programas\TEMA.txt")
        for linea in f:
            info = linea.strip().split('|')
            if info[0] == busqueda:
                print(linea)
        f.close()