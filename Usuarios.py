import csv #Importar Modulo
import os
nombre_archivo = "Usuarios.csv"
ruta= os.path.abspath(__file__)
directorio= os.listdir(os.path.dirname(ruta))
print('los directorios son: ', directorio, "y se encuentran en la ruta:", os.path.dirname(ruta), '\n')
with open(nombre_archivo, "r") as archivo:
    users = csv.reader(archivo, delimiter='\n')
    for dato in users:
        print("N° Columnas =", len(dato))
        