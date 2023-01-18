# Hacer un programa que pida al usuario ingresar por consola un numero haciendo referencia a los años
# y que el programa identifique por grupos de años que etapa de la boda esta

num = int(input("Ingresa la cantidad de años: "))

if num >= 0 and num <= 4:
    print("Usted esta en las bodas de Papel")
elif num >= 5 and num <= 9:
    print("Usted esta en las bodas de madera")
elif num >= 10 and num <= 14:
    print("Usted esta en las bodas de aluminio o estaño")
elif num >= 15 and num <= 19 :
    print("Usted esta en las bodas de cristal")
elif num >= 20 and num <= 24:
    print("Usted esta en las bodas de porcelana")
elif num >= 25 and num <= 29 :
    print("usted esta en las bodas de plata")
elif num >= 30 and num <= 39 :
    print("usted esta en las bodas de perlas")
elif num >= 40 and num <= 49 :
    print("usted esta en las bodas de rubi")
elif num >= 50 and num <= 59 :
    print("usted esta en las bodas de oro")
else : print("Usted es todo un campeon")

