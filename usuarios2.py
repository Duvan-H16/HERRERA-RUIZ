import csv #Importar Modulo
nombre_archivo = "Usuarios.csv"
with open(nombre_archivo, mode='r') as archivo:
    users = csv.reader(archivo)
    for dato in users:
        print(dato)