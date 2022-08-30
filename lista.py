from nodo import Datospaciente
from nodomatriz import Datosmatriz
from listamatriz import listamatriz
import numpy as np
import math

listam=listamatriz()
class listasi():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
        self.numerito=1
        global matrizenferma

    

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
                    self.numerito=self.numerito+1
                else:
                    print("Nombre: ", tmp.nombre, "\n", "Edad: ", tmp.edad, "\n", "Períodos:  ", tmp.periodos, "\n", "Tamaño de matriz:  ", tmp.m, "\n", "Período inicial:", "\n",  tmp.celda)
                    global matrizenferma
                    global tamañomatriz
                    global periodosenferma
                    matrizenferma=tmp.celda
                    periodosenferma=int(tmp.periodos)
                    tamañomatriz=int(tmp.m)
                    break
            

    def mostrarmatrizenferma(self):
        global matrizenmatriz
        matrizenmatriz=np.array(matrizenferma)
        coordenadasenfermas1=[]
        coordenadasenfermas2=[]
        sumadematrices=[]
        periodossuma=1


        while periodossuma <=periodosenferma:
            #Ciclo para la restricción de células sanas
            numerito=1
            for i in matrizenmatriz:
                
                numerito2=1
                for j in i:
                    if numerito2<=tamañomatriz-2 and numerito<=tamañomatriz-2 and matrizenmatriz[numerito][numerito2]==0:
                        celulaenferma=0
                        if matrizenmatriz[numerito-1][numerito2-1]==1:
                            celulaenferma+=1
                        if matrizenmatriz[numerito][numerito2-1]==1:
                            celulaenferma+=1
                        if matrizenmatriz[numerito+1][numerito2-1]==1:
                            celulaenferma+=1
                        if matrizenmatriz[numerito-1][numerito2]==1:
                            celulaenferma+=1
                        if matrizenmatriz[numerito+1][numerito2]==1:
                            celulaenferma+=1
                        if matrizenmatriz[numerito-1][numerito2+1]==1:
                            celulaenferma+=1
                        if matrizenmatriz[numerito][numerito2+1] ==1:
                            celulaenferma+=1
                        if matrizenmatriz[numerito+1][numerito2+1]==1:
                            celulaenferma+=1
                        if celulaenferma==3:
                            coordenadasenfermas1.append((numerito))
                            coordenadasenfermas2.append((numerito2))
                    numerito2+=1 
                numerito+=1 





            coordenadasenfermas11=[]
            coordenadasenfermas21=[]


            #Ciclo para la restricción de células enfermas
            iteradorenfermo=1
            for i in matrizenmatriz:
                
                iteradorenfermo2=1
                for j in i:
                    if iteradorenfermo2<=tamañomatriz-2 and iteradorenfermo<=tamañomatriz-2 and matrizenmatriz[iteradorenfermo][iteradorenfermo2]==1:
                        celulaenferma2=0
                        if matrizenmatriz[iteradorenfermo-1][iteradorenfermo2-1]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorenfermo][iteradorenfermo2-1]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorenfermo+1][iteradorenfermo2-1]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorenfermo-1][iteradorenfermo2]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorenfermo+1][iteradorenfermo2]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorenfermo-1][iteradorenfermo2+1]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorenfermo][iteradorenfermo2+1]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorenfermo+1][iteradorenfermo2+1]==1:
                            celulaenferma2+=1
                        if celulaenferma2==3 or celulaenferma2==2:
                            coordenadasenfermas11.append((iteradorenfermo))
                            coordenadasenfermas21.append((iteradorenfermo2))
                    iteradorenfermo2+=1 
                iteradorenfermo+=1 




            coordenadasenfermas13=[]
            coordenadasenfermas23=[]



            #Ciclo para la restricción de células enfermas a células sanas
            iteradorsano=1
            for i in matrizenmatriz:
                
                iteradorsano2=1
                for j in i:
                    if iteradorsano2<=tamañomatriz-2 and iteradorsano<=tamañomatriz-2 and matrizenmatriz[iteradorsano][iteradorsano2]==1:
                        celulaenferma2=0
                        if matrizenmatriz[iteradorsano-1][iteradorsano2-1]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorsano][iteradorsano2-1]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorsano+1][iteradorsano2-1]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorsano-1][iteradorsano2]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorsano+1][iteradorsano2]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorsano-1][iteradorsano2+1]==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorsano][iteradorsano2+1] ==1:
                            celulaenferma2+=1
                        if matrizenmatriz[iteradorsano+1][iteradorsano2+1]==1:
                            celulaenferma2+=1
                        if celulaenferma2!=3 or celulaenferma2!=2:
                            coordenadasenfermas13.append((iteradorsano))
                            coordenadasenfermas23.append((iteradorsano2))
                    iteradorsano2+=1 
                iteradorsano+=1 





            #actualizador de células enfermas a sanas
            actualizador2=0
            for l in range(len(coordenadasenfermas13)):
                matrizenmatriz[(coordenadasenfermas13[actualizador2])][(coordenadasenfermas23[actualizador2])]=0
                actualizador2+=1



            #actualizador de células sanas a enfermas
            actualizador=0
            for l in range(len(coordenadasenfermas1)):
                matrizenmatriz[(coordenadasenfermas1[actualizador])][(coordenadasenfermas2[actualizador])]=1
                actualizador+=1



            #actualizador de células enfermas que siguen enfermas
            actualizador1=0
            for l in range(len(coordenadasenfermas11)):
                matrizenmatriz[(coordenadasenfermas11[actualizador1])][(coordenadasenfermas21[actualizador1])]=1
                actualizador1+=1

            print("Patrón No." + str(periodossuma))                
            print(matrizenmatriz)
            periodossuma+=1
            sumadematrices.append(matrizenmatriz)
            if periodossuma <=12:
                seguir= input("¿Desea seguir analizando la muestra?: \n1. Si \n2. Salir del programa \n")
                if seguir==2:
                    print("¡Regresa pronto! :)")
                    quit()











    def mostrarlista(self):
        tmp = self.primero
        while tmp is not None:
            print("Nombre: ", tmp.nombre, "\n", "Edad: ", tmp.edad, "\n", "Períodos:  ", tmp.periodos, "\n", "Tamaño de matriz:  ", tmp.m, "\n", tmp.celda)
            tmp=tmp.getsiguiente()




