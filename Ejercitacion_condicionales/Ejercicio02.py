# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Ingrese su edad: "))

if edad <= 17 : #si es mayor o igual a 17 imprimir
    print("Usted es menor")
else:
    print("Usted es adulto responsable")