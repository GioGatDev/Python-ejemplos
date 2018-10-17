n = int(input("Dame un numero entero: "))
def factorial( n ):
   if n == 1:   
       return n
   else:
       #llamada recursiva
       return n * factorial( n - 1 )  
print("El factorial de: ",n,"es", factorial(n))