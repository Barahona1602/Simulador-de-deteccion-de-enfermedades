class Datosmatriz():
    def __init__(self, matriz):
        self.matriz=matriz
        self.siguiente = None



    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, siguiente):
        self.siguiente= siguiente