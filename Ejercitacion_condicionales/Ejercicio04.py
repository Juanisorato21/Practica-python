#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

#Mi solucion
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

if num1/num2 == 0:
    print("Error")
else: print(num1/num2)

#Otra solucion
n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisior: "))
if m == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(n/m)