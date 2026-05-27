with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    print(linea.strip())