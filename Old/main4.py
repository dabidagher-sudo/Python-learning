def analizar_linea(temp,presion):
    if temp>30:
        return "Alarma Temperatura"
    elif presion<50:
        return "Presion baja"
    else:
        return "Ok"
#Contadores
Alarma=0
AlTemp=0
AlPresion=0
Ok=0

with open("reporte1.txt", "w") as salida:
    with open("datos1.csv","r") as archivo:
        for linea in archivo:
            partes=linea.split(",")
            temp=int(partes[0])
            presion=int(partes[1])
            resultado= analizar_linea(temp,presion)
            print("temp= ",temp,"presion= ",presion,"->", resultado)
            salida.write(f"temp= {temp} presion= {presion} -> {resultado}\n")
            if resultado=="Alarma Temperatura":
                Alarma+=1
                AlTemp+=1
            elif resultado=="Presion baja":
                Alarma+=1
                AlPresion+=1
            else:
                Ok+=1
#imprimir totales
    print("\nResumen: ")
    print("Total Alarmas= ", Alarma)
    print("Total Alarmas Temperatura= ", AlTemp)
    print("Total Alarmas Presion= ", AlPresion)
    print("Total Ok= ",Ok)
    salida.write(f"\nResumen")
    salida.write(f"\nTotal Alarmas= {Alarma}")
    salida.write(f"\nTotal Alarmas Temperatura= {AlTemp}")
    salida.write(f"\nTotal Alarmas Presion= {AlPresion}")
    salida.write(f"\nTotal Ok= {Ok}")

