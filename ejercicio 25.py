h=int(input("ingresa la hora: "))
m=int(input("ingresa minuto: "))
s=int(input("ingresa segundo: "))
if(h<24 and m<60 and s<60):
    if(s<59 and s>=0):
        print(str(h)+"h "+str(m)+"m "+str(s+1)+"s")
else:
    if(s==59):
        print("El segundo es: ")
    elif(m==59):
        print("El minuto es: ")
    if(h==23):
        print("00h 00m 00s")
    else:
        print(str(h+1)+"h 00m 00s")       


    
    
    


    
