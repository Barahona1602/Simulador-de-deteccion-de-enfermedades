from tkinter import filedialog
from xml.dom import minidom
from tkinter import filedialog as fd
import xml.etree.ElementTree as ET

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
        nombre = datos.getElementsByTagName('nombre')
        edad = datos.getElementsByTagName('edad')
        periodos = datos.getElementsByTagName('periodos')
        m = datos.getElementsByTagName('m')

#Opción de salir
elif numero=="2":
    print("¡Regresa pronto! :)")
    quit()

#Cambios deben de aparecer
