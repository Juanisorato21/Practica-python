# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra = input("Ingrese una palabra: ")
rango = int(input("Ingrese la cantidad de veces que quieres que se repita: "))

for i in range(rango):
    print(palabra)