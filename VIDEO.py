class VIDEO:
    def __init__(self, id_video, nombre, url, fecha_publicacion):
        self.__id_video = id_video
        self.__nombre = nombre
        self.__url = url
        self.__fecha_publicacion = fecha_publicacion

    def guardar(self):
        f = open("c:\Programas\VIDEO.txt","a", encoding="utf8")
        f.write(str(self.__id_video)+'|')
        f.write(str(self.__nombre)+'|')
        f.write(str(self.__url)+'|')
        f.write(str(self.__fecha_publicacion)+'\n')
        f.close()

    @classmethod
    def consultar_por_id(cls):
        busqueda = input("**Consulta datos por id** Inserte id a consultar:")
        f = open("c:\Programas\VIDEO.txt")
        for linea in f:
            info = linea.strip().split('|')
            if info[0] == busqueda:
                print(linea)
        f.close()
        
    def consultar_todo(self):
        f = open("c:\Programas\VIDEO.txt")
        print(f.read())
        f.close()