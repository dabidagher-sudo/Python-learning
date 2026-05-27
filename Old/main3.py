def analizar_linea(linea):
    partes = linea.split(",")

    temp=int(partes[0].split("=")[1])
    presion=int(partes[1].split("=")[1])

    if temp>30:
        return "Alarma temperatura"
    elif presion<50:
        return "Baja presion"
    else:
        return "OK"
with open("datos.txt","r") as archivo:
    for linea in archivo:
        resultado= analizar_linea(linea.strip())
        print(linea.strip(),"->", resultado)

with open("reporte.txt", "w") as salida:
    with open("datos.txt","r") as archivo:
        for linea in archivo:
            resultado=analizar_linea(linea.strip())
            salida.write(f"{linea.strip()} -> {resultado}\n")