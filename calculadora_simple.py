def num():
    global a,b
    a=int(input("Ingrese el primer número:\n"))
    b=int(input("Ingrese el segundo número:\n"))
    
def suma():
    print("El resultado de la suma de: ",a,"+",b,"es:",a+b)
def resta():
    print("El resultado de la resta de: ",a,"-",b,"es:",a-b)
def multiplicacion():
    print("El resultado de la multiplicación de: ",a,"*",b,"es:",a*b)
def division():
    print("El resultado de la división de: ",a,"/",b,"es:",a/b)
    
while(True):
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División")
    opcion = int(input("Ingrese la opción\n"))
    if(opcion == 1):
        num()
        suma()
    elif(opcion == 2):
        num()
        resta()
    elif(opcion == 3):
        num()
        multiplicacion()
    elif(opcion == 4):
        num()
        division()