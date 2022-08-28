from nodo import Datospaciente
class listasi():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
    

    def siginsert(self, numpaciente, nombre, edad, periodos, m, rejilla, celda):
        global paciente2
        paciente2= Datospaciente(numpaciente, nombre, edad, periodos, m, rejilla, celda)
        self.size += 1
        if self.primero is None:
            self.primero = paciente2
            self.ultimo= paciente2
        else:
            tmp = self.primero
            while tmp.getsiguiente() is not None:
                tmp=tmp.getsiguiente()
            tmp.setsiguiente(paciente2)
    

    def mostrarpaciente(self):
        tmp = self.primero
        conteo=0
        while tmp is not None:
            conteo=conteo+1
            print("Paciente: ", tmp.numpaciente)
            print("Nombre: ", tmp.nombre)
            tmp=tmp.getsiguiente()



    def pacienteseleccionado(self, numpaciente2):
        tmp = self.primero
        while tmp is not None:
                if numpaciente2 != tmp.numpaciente:
                    tmp=tmp.getsiguiente()
                else:
                    print("Nombre: ", tmp.nombre, "\n", "Edad: ", tmp.edad, "\n", "Períodos:  ", tmp.periodos, "\n", "Tamaño de matriz:  ", tmp.m, "\n", tmp.celda)
                    break
            





        
    def mostrarlista(self):
        tmp = self.primero
        while tmp is not None:
            print("Nombre: ", tmp.nombre, "\n", "Edad: ", tmp.edad, "\n", "Períodos:  ", tmp.periodos, "\n", "Tamaño de matriz:  ", tmp.m, "\n", tmp.celda)
            tmp=tmp.getsiguiente()

