from datetime import datetime

while True:
    try:
        fecha = input("Ingresa una fecha en el formato Día/Mes/Año: ")
        datetime.strptime(fecha, '%d/%m/%Y')
        print("Fecha válida")
    except ValueError:
        print("Fecha inválida")