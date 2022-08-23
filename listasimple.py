from nodo import Datospaciente
class listasi():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
    
    
    def siginsert(self, nombre, edad, periodos, m, rejilla, celda):

        paciente2= Datospaciente(nombre, edad, periodos, m, rejilla, celda)
        self.size += 1
        if self.primero is None:
            self.primero = paciente2
            self.ultimo= paciente2
        else:
            tmp = self.primero
            while tmp.getsiguiente() is not None:
                tmp=tmp.getsiguiente()
            tmp.setsiguiente(paciente2)
        
    def mostrarlista(self):
        tmp = self.primero
        print(self.size)
        while tmp is not None:
            print("Nombre: ", tmp.nombre, "   ", "Edad: ", tmp.edad, "  ", "Períodos:  ", tmp.periodos, " ", "Matriz:  ", tmp.m, "Rejilla: ",  tmp.rejilla, "Celda: ", tmp.celda)
            tmp=tmp.getsiguiente()
    