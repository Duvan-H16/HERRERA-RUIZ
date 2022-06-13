import csv #Importar Modulo
import os
nombre_archivo = "Usuarios.csv"
ruta= os.path.abspath(__file__)
directorio= os.listdir(os.path.dirname(ruta))
print('los directorios son: ', directorio, "y se encuentran en la ruta:", os.path.dirname(ruta), '\n')
with open(nombre_archivo, "r") as archivo:
    users = csv.DictReader(archivo)
    for dato in users:
        clave = list(dato.keys())
        print(clave[1], dato['Nombres'], clave[2], dato['Apellidos'], clave[4], dato['Dependencia'], clave[10], dato["Estado"], "N° Columnas =", len(dato))