from nodo import Datospaciente
import numpy as np
from iteration_utilities import duplicates
import xml.etree.cElementTree as ET
from bs4 import BeautifulSoup
import pandas as pd
from collections import OrderedDict


class listasi():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
        self.nums=1
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
                    self.nums=self.nums+1
                else:
                    print("Nombre: ", tmp.nombre, "\n", "Edad: ", tmp.edad, "\n", "Períodos:  ", tmp.periodos, "\n", "Tamaño de matriz:  ", tmp.m, "\n", "Período inicial:", "\n",  tmp.celda)
                    global nombreselec
                    global edadselec
                    global matrizenferma
                    global tamañomatriz
                    global periodosenferma
                    nombreselec=tmp.nombre
                    edadselec=tmp.edad
                    matrizenferma=tmp.celda
                    periodosenferma=int(tmp.periodos)
                    tamañomatriz=int(tmp.m)
                    break
            

    def mostrarmatrizenferma(self):
        global matrizenmatriz
        matrizenmatriz=np.array(matrizenferma)
        global sumadematrices
        sumadematrices=[]
        
        periodossuma=1


        while periodossuma <=periodosenferma:
                
                


            #Ciclo para la restricción de células enfermas a células sanas
            coordenadasenfermas13=[]
            coordenadasenfermas23=[]
            iteradorsano=0
            for i in matrizenmatriz:
                
                celulaenferma3=0
                iteradorsano2=0
                for j in i:
                    if iteradorsano2<=tamañomatriz-1 and iteradorsano<=tamañomatriz-1 and matrizenmatriz[iteradorsano][iteradorsano2]==1:
                        celulaenferma3=0
                        if iteradorsano!=0 and iteradorsano2!=0 and matrizenmatriz[iteradorsano-1][iteradorsano2-1]==1:
                            celulaenferma3+=1
                        if iteradorsano!=0 and matrizenmatriz[iteradorsano][iteradorsano2-1]==1:
                            celulaenferma3+=1
                        if iteradorsano!=tamañomatriz-1 and iteradorsano2!=0 and matrizenmatriz[iteradorsano+1][iteradorsano2-1]==1:
                            celulaenferma3+=1
                        if iteradorsano!=0 and matrizenmatriz[iteradorsano-1][iteradorsano2]==1:
                            celulaenferma3+=1
                        if iteradorsano!=tamañomatriz-1 and matrizenmatriz[iteradorsano+1][iteradorsano2]==1:
                            celulaenferma3+=1
                        if iteradorsano!=0 and iteradorsano2!=tamañomatriz-1 and matrizenmatriz[iteradorsano-1][iteradorsano2+1]==1:
                            celulaenferma3+=1
                        if iteradorsano2!=tamañomatriz-1 and matrizenmatriz[iteradorsano][iteradorsano2+1] ==1:
                            celulaenferma3+=1
                        if iteradorsano!=tamañomatriz-1 and iteradorsano2!=tamañomatriz-1 and matrizenmatriz[iteradorsano+1][iteradorsano2+1]==1:
                            celulaenferma3+=1
                        if celulaenferma3!=3 or celulaenferma3!=2:
                            coordenadasenfermas13.append((iteradorsano))
                            coordenadasenfermas23.append((iteradorsano2))
                    iteradorsano2+=1 
                iteradorsano+=1 
            


            #Ciclo para la restricción de células sanas
            coordenadasenfermas1=[]
            coordenadasenfermas2=[]
            numerito=0
            for i in matrizenmatriz:
                
                celulaenferma=0
                numerito2=0
                for j in i:
                    if numerito2<=tamañomatriz-1 and numerito<=tamañomatriz-1 and matrizenmatriz[numerito][numerito2]==0:
                        celulaenferma=0
                        if numerito!=0 and numerito2!=0 and matrizenmatriz[numerito-1][numerito2-1]==1:
                            celulaenferma+=1
                        if numerito2!=0 and matrizenmatriz[numerito][numerito2-1]==1:
                            celulaenferma+=1
                        if numerito!=tamañomatriz-1 and numerito2!=0 and matrizenmatriz[numerito+1][numerito2-1]==1:
                            celulaenferma+=1
                        if numerito!=0 and matrizenmatriz[numerito-1][numerito2]==1:
                            celulaenferma+=1
                        if numerito!=tamañomatriz-1 and matrizenmatriz[numerito+1][numerito2]==1:
                            celulaenferma+=1
                        if numerito!=0 and numerito2!=tamañomatriz-1 and matrizenmatriz[numerito-1][numerito2+1]==1:
                            celulaenferma+=1
                        if numerito2!=tamañomatriz-1 and matrizenmatriz[numerito][numerito2+1]==1:
                            celulaenferma+=1
                        if numerito!=tamañomatriz-1 and numerito2!=tamañomatriz-1 and matrizenmatriz[numerito+1][numerito2+1]==1:
                            celulaenferma+=1
                        if celulaenferma==3:
                            coordenadasenfermas1.append((numerito))
                            coordenadasenfermas2.append((numerito2))
                    numerito2+=1 
                numerito+=1 



            
            #Ciclo para la restricción de células enfermas
            coordenadasenfermas11=[]
            coordenadasenfermas21=[]
            iteradorenfermo=0
            for i in matrizenmatriz:

                celulaenferma=0
                iteradorenfermo2=0
                for j in i:
                    if iteradorenfermo2<=tamañomatriz-1 and iteradorenfermo<=tamañomatriz-1 and matrizenmatriz[iteradorenfermo][iteradorenfermo2]==1:
                        celulaenferma2=0
                        if iteradorenfermo!=0 and iteradorenfermo2!=0 and matrizenmatriz[iteradorenfermo-1][iteradorenfermo2-1]==1:
                            celulaenferma2+=1
                        if iteradorenfermo2!=0 and matrizenmatriz[iteradorenfermo][iteradorenfermo2-1]==1:
                            celulaenferma2+=1
                        if iteradorenfermo!=tamañomatriz-1 and iteradorenfermo2!=0 and matrizenmatriz[iteradorenfermo+1][iteradorenfermo2-1]==1:
                            celulaenferma2+=1
                        if iteradorenfermo!=0 and matrizenmatriz[iteradorenfermo-1][iteradorenfermo2]==1:
                            celulaenferma2+=1
                        if iteradorenfermo!=tamañomatriz-1 and matrizenmatriz[iteradorenfermo+1][iteradorenfermo2]==1:
                            celulaenferma2+=1
                        if iteradorenfermo!=0 and iteradorenfermo2!=tamañomatriz-1 and matrizenmatriz[iteradorenfermo-1][iteradorenfermo2+1]==1:
                            celulaenferma2+=1
                        if iteradorenfermo2!=tamañomatriz-1 and matrizenmatriz[iteradorenfermo][iteradorenfermo2+1]==1:
                            celulaenferma2+=1
                        if iteradorenfermo!=tamañomatriz-1 and iteradorenfermo2!=tamañomatriz-1 and matrizenmatriz[iteradorenfermo+1][iteradorenfermo2+1]==1:
                            celulaenferma2+=1
                        if celulaenferma2==3 or celulaenferma2==2:
                            coordenadasenfermas11.append((iteradorenfermo))
                            coordenadasenfermas21.append((iteradorenfermo2))
                    iteradorenfermo2+=1 
                iteradorenfermo+=1 




            #actualizador de células enfermas a sanas
            actualizador2=0
            for l in range(len(coordenadasenfermas13)):
                matrizenmatriz[(coordenadasenfermas13[actualizador2])][(coordenadasenfermas23[actualizador2])]=0
                actualizador2+=1

            #actualizador de células enfermas que siguen enfermas
            actualizador1=0
            for l in range(len(coordenadasenfermas11)):
                matrizenmatriz[(coordenadasenfermas11[actualizador1])][(coordenadasenfermas21[actualizador1])]=1
                actualizador1+=1

            #actualizador de células sanas a enfermas
            actualizador=0
            for l in range(len(coordenadasenfermas1)):
                matrizenmatriz[(coordenadasenfermas1[actualizador])][(coordenadasenfermas2[actualizador])]=1
                actualizador+=1




            print("Patrón No." + str(periodossuma))                
            print(matrizenmatriz)
            periodossuma+=1
            sumadematrices.append(matrizenmatriz)
            
            
            
            
            if periodossuma <=periodosenferma:
                seguir= input("¿Desea seguir analizando la muestra?: \n1. Si \n2. Salir del programa \n")
                if seguir==2:
                    print("¡Regresa pronto! :)")
                    quit()


    def listaduplicada(self):
        global resultadoselec
        global resultadosumadematrices
        resultadosumadematrices=[]
        track=[]
        resultadoselec=""
        enfermedadgrave=False
        enfermedadmortal=False
        sanito=False
        count=0
        

        resultadosumadematrices=list(duplicates(sumadematrices))




        if (len(resultadosumadematrices)>2):
            enfermedadgrave=True
            resultadoselec="grave"
        
        elif (len(resultadosumadematrices)==2):
            enfermedadmortal=True
            resultadoselec="mortal"

        elif (len(resultadosumadematrices)<1):
            sanito=True
            resultadoselec="leve"



    def generarxml(self):

       pacientes=ET.Element("pacientes")
       paciente = ET.SubElement(pacientes, "paciente")
       datospersonales = ET.SubElement(paciente, "datospersonales")
       nombre= ET.SubElement(datospersonales, "nombre").text=nombreselec
       edad= ET.SubElement(datospersonales, "edad").text=edadselec
       periodos = ET.SubElement(paciente, "periodos").text=str(periodosenferma)
       resultado = ET.SubElement(paciente, "resultado").text=resultadoselec 

       archivo = ET.ElementTree(pacientes)
       ET.indent(archivo)
       archivo.write(("paciente_"+nombreselec+".xml"))






