numero = int (input ('Ingresa el valor de numero: '))
invertido=(numero%100000-numero%10000)//10000+(numero%10000-numero%1000)//100+(numero%1000-numero%100)+(numero%100-numero%10)*100+(numero%10)*10000
print ('Valor de invertido: ' + repr (invertido))
print ()
    