class Datospaciente():
    def __init__(self, nombre, edad, periodos, m):
        self.nombre=nombre
        self.edad=edad
        self.periodos=periodos
        self.m=m
        self.siguiente=None
    


    def getsiguiente(self):
        return self.siguiente



    def setsiguiente(self, siguiente):
        self.siguiente= siguiente