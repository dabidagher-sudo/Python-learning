def revisar(temp):
    if temp > 30:
        return "Alarma Temperatura"
    return "Temperatura Ok"

def revisar1(presion):
    if presion < 50:
        return "Presion Baja"
    return "Presion OK"

print(revisar(23))
print(revisar1(55))