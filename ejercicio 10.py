
n = float(input("ingrese los segundos: "))

if n >= 0:
    hrs = int(n/3600)
    tiempo = n % 3600
    min = int(tiempo/60)
    seg = tiempo % 60
    print("la convercion es: ", hrs, ":", min, ":", seg)
else:
    print("error el numero no debe ser cero")
