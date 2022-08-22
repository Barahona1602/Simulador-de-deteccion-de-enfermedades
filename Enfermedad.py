from tkinter import filedialog
from xml.dom import minidom
from tkinter import filedialog as fd
import xml.etree.ElementTree as ET
from listasimple import listasi

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
        listasimple.siginsert(nombre[0].firstChild.data, edad[0].firstChild.data, periodos[0].firstChild.data, m[0].firstChild.data)

    listasimple.mostrarlista()

#Opción de salir
elif numero=="2":
    print("¡Regresa pronto! :)")
    quit()


