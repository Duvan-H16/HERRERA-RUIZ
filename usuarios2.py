import csv #Importar Modulo

with open(csv.Usuarios) as archivo:
    users = csv.reader(archivo)
    for dato in users:
        clave = list(dato.keys())
        print(clave[1], dato["Nombres"], clave[2], dato["Apellidos"], clave[4], dato["Dependencia"], clave[10], dato["Estado"], "N° Columnas =", len(dato))