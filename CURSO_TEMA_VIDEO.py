class CURSO_TEMA_VIDEO:

    def __init__(self, id_CTV, id_CT, id_video):
        
        self.__id_CTV = id_CTV
        self.__id_CT = id_CT
        self.__id_video = id_video

    def guardar(self):
        f = open("c:\Programas\CURSO_TEMA_VIDEO.txt","a", encoding="utf8")
        f.write(str(self.__id_CTV)+'|')
        f.write(str(self.__id_CT)+'|')
        f.write(str(self.__id_video)+ '\n')
        f.close()

    def consultar_todo(self):
        f = open("c:\Programas\CURSO_TEMA_VIDEO.txt")
        print(f.read())
        f.close()
