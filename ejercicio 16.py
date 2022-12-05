

print("ingrese los tres numeros:")
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 > n2:
    if n1 > n3:
        m = n1
    else:
        m = n3
else:
    if n2 > n3:
        m = n2
    else:
        m = n3
print("el numero mayor es: ", m)
