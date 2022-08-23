class Datospaciente():
    def __init__(self, nombre, edad, periodos, m, rejilla, celda):
        self.nombre=nombre
        self.edad=edad
        self.periodos=periodos
        self.m=m
        self.rejilla=rejilla
        self.celda=celda
        self.siguiente=None
    


    def getsiguiente(self):
        return self.siguiente



    def setsiguiente(self, siguiente):
        self.siguiente= siguiente