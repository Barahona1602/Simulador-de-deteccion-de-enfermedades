from selectors import SelectSelector
from tkinter import filedialog
from xml.dom import minidom
from tkinter import filedialog as fd
import xml.etree.ElementTree as ET
from lista import listasi
import numpy as np
from nodo import Datospaciente
from listamatriz import listamatriz

listam = listamatriz()
listasimple=listasi()


#Menú principal
print("Bienvenido al programa de enfermedades")
print("Me llamo Pablo Barahona y soy quien realizó el programa")
print("Mi curso es Introducción a la Programación 2 sección D")
print("Mi carnet es 202109715")
numero = input('Ingrese "1" si quiere ingresar sus datos, ingrese "2" si quiere salir: ')


if numero=="1":
    print("Gracias por ingresar")

    #Abrir archivos (XML y todos los archivos)
    archivo = filedialog.askopenfilename(title="abrir", initialdir="C:/", filetypes=(("XML files",".XML"),("Todos los archivos",".*")))
    datos = minidom.parse(archivo)
    pacientes = datos.getElementsByTagName('pacientes')
    paciente = datos.getElementsByTagName('paciente')
    numpaciente=0

    #Leer archivo XML con dom
    for i in paciente:
        numpaciente=numpaciente+1
        nombre = i.getElementsByTagName('nombre')
        edad = i.getElementsByTagName('edad')
        periodos = i.getElementsByTagName('periodos')
        m = i.getElementsByTagName('m')
        rejilla = i.getElementsByTagName('rejilla')
        celda= i.getElementsByTagName('celda')


        #Leer la matriz con celdas contagiadas
        num= int(m[0].firstChild.data)
        matriz = np.zeros((num,num))
        for j in rejilla:
            num=0
            for k in celda:
                matriz[(int(celda[num].attributes['f'].value))][(int(celda[num].attributes['c'].value))]=1
                num+=1
            orden=np.zeros((num,2))
            p=0
            for l in celda:
                orden[p][0]=(int(celda[p].attributes['f'].value))
                orden[p][1]=(int(celda[p].attributes['c'].value))
                p+=1

        #Guardar datos en nodo
        listasimple.siginsert(numpaciente, nombre[0].firstChild.data, edad[0].firstChild.data, periodos[0].firstChild.data, m[0].firstChild.data, orden, matriz)


    #Método para mostrar los datos de la lista (nombre y numero de paciente)
    listasimple.mostrarpaciente()
    seleccionarp = input("Seleccione el paciente según su número: ")
    sele=int(seleccionarp)

    #Método para mostrar el paciente que seleccionó el usuario
    listasimple.pacienteseleccionado(sele)


    leer= input("¿Desea analizar la muestra?: \n1. Si \n2. Salir del programa \n")

    if leer=="1":
        listasimple.mostrarmatrizenferma()
    elif leer=="2":
        print("¡Regresa pronto! :)")
        quit()






#Opción de salir
elif numero=="2":
    print("¡Regresa pronto! :)")
    quit()


