#monitor test
def analizar_maquina (temp, presion):
    if temp > 30:
        return "Alarma Temperatura"
    elif presion < 50:
        return "Presion Baja"
    else:
        return "Ok"

def leer_datos (nombre_archivo):
    datos = []

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")

            temp = int(partes[0])
            presion = int(partes[1])

            datos.append((temp,presion))

    return datos

def generar_reporte(datos):
    alarma = 0
    al_temp = 0
    al_presion = 0
    ok = 0
    total = 0
    lineas_reporte = []

    for temp, presion in datos:
        resultado = analizar_maquina(temp, presion)

        lineas_reporte.append(
            f"temp={temp}, presion= {presion} -> {resultado}"
        )

        if resultado == "Alarma Temperatura":
            alarma += 1
            al_temp += 1
        elif resultado == "Presion Baja":
            alarma += 1
            al_presion += 1
        else:
            ok += 1
    
    total = len(datos)
    lineas_reporte.append("")
    lineas_reporte.append("Resumen")
    lineas_reporte.append(f"Total Alarmas: {alarma}")
    lineas_reporte.append(f"Total Alarmas Temperatura: {al_temp}")
    lineas_reporte.append(f"Total Alarmas Presion: {al_presion}")
    lineas_reporte.append(f"Total Ok: {ok}")
    lineas_reporte.append(f"Total de Registros Analizados: {total}")

    return lineas_reporte

def guardar_reporte(nombre_archivo, lineas_reporte):
    with open(nombre_archivo, "w") as archivo:
        for linea in lineas_reporte:
            archivo.write(linea + "\n")
