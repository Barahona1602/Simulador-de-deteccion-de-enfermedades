from nodomatriz import Datosmatriz
class listamatriz():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
    
    def sigmatriz(self, matriz):
        mamarre= Datosmatriz(matriz)
        self.size += 1
        if self.primero is None:
            self.primero = mamarre
            self.ultimo= mamarre
        else:
            tmp2 = self.primero
            while tmp2.getsiguiente() is not None:
                tmp2=tmp2.getsiguiente()
            tmp2.setsiguiente(mamarre)
    
    
    def mostrarmatriz(self):
        print("Si imprime 1")
        tmp2 = self.primero
        print("Si imprime 2")
        print("Matriz enferma: ", tmp2.matriz)