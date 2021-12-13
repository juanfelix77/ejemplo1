class Avionica():
    def __init__(self,tipo,serie,unidad):
        self.tipo=tipo
        self.serie=serie
        self.unidad=unidad

    def operatividad(self):
        print("operativo")

    def equipo(self):
        print("EQUIPO:",self.tipo,"MODELO:",self.modelo)

class Comunicaciones(Avionica):
    def __init__(self,tipo,serie,unidad,modelo):
        super().__init__(tipo,serie,unidad)
        self.modelo=modelo

comuni=Comunicaciones("VHF","M345","GRUPO11","ARC159")
comuni.equipo()


