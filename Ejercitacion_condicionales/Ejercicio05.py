#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

n = int(input("Ingrese un numero: "))

if n % 2 == 0:
    print("Su numero es par")
else: print("Su numero es impar")