#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña_input = input("Ingrese una contraseña: ")
contraseña_local = "M1000"
if contraseña_input == "M1000":
    print("Ingreso exitoso")
else: print("Contraseña incorrecta")
