from tkinter import filedialog
from xml.dom import minidom
from tkinter import filedialog as fd
import xml.etree.ElementTree as ET
from lista import listasi
import numpy as np

listasimple=listasi()
print("Bienvenido al programa de enfermedades")
print("Me llamo Pablo Barahona y soy quien realizó el programa")
print("Mi curso es Introducción a la Programación 2 sección D")
print("Mi carnet es 202109715")
numero = input('Ingrese "1" si quiere ingresar sus datos, ingrese "2" si quiere salir: ')


if numero=="1":
    print("Gracias por ingresar")
    archivo = filedialog.askopenfilename(title="abrir", initialdir="C:/", filetypes=(("XML files",".XML"),("Todos los archivos",".*")))
    datos = minidom.parse(archivo)
    pacientes = datos.getElementsByTagName('pacientes')
    paciente = datos.getElementsByTagName('paciente')

    for i in paciente:
        nombre = i.getElementsByTagName('nombre')
        edad = i.getElementsByTagName('edad')
        periodos = i.getElementsByTagName('periodos')
        m = i.getElementsByTagName('m')
        rejilla = i.getElementsByTagName('rejilla')
        celda= i.getElementsByTagName('celda')

        num= int(m[0].firstChild.data)
        matriz = np.zeros((num,num))
        for j in rejilla:
            num=0
            for k in celda:
                matriz[(int(celda[num].attributes['f'].value)-1)][(int(celda[num].attributes['c'].value)-1)]=1
                num+=1
            orden=np.zeros((num,2))
            p=0
            for l in celda:
                orden[p][0]=(int(celda[p].attributes['f'].value))
                orden[p][1]=(int(celda[p].attributes['c'].value))
                p+=1
        
        
        
        listasimple.siginsert(nombre[0].firstChild.data, edad[0].firstChild.data, periodos[0].firstChild.data, m[0].firstChild.data, orden, matriz)

    listasimple.mostrarlista()

#Opción de salir
elif numero=="2":
    print("¡Regresa pronto! :)")
    quit()


