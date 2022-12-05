
# /Definir variables

num1 = int(input("Ingrese el primer numero: "))
print("Ingrese el segundo numero: ")
num2 = int(input())
# Calculos
suma1 = 0
suma2 = 0
for i in range(1,num1):
	if num1%i==0:
		suma1 = suma1+i
for i in range(1,num2):
	if num2%i==0:
		suma2 = suma2+i
# Mostrar resultados
if suma1==num2 and suma2==num1:
	print(num1," y ",num2," son amigos")
else:
	print(num1," y ",num2," no son amigos")

