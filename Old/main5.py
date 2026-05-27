#Main programa
from monitor import leer_datos, generar_reporte, guardar_reporte

datos = leer_datos("datos1.csv")
reporte = generar_reporte(datos)

for linea in reporte:
    print(linea)

guardar_reporte("reporte2.txt", reporte)