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