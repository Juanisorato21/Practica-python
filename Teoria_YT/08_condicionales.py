###Condicionales###

#Si la condicion de mi_condicional es True se ejecuta el if, si es false se ejecuta el else
mi_condicional = False


if mi_condicional: #Es lo mismo que if mi_condicional ==True:
    print("Se ejecuta la condicion del if")
else: print("Se ejecuta la condicion del else")
    
#Si la condicion de mi_condicional es 10 se ejecuta el if, de lo contrario se ejecuta el else
mi_condicional = 5 * 0

if mi_condicional == 10: #si mi condicion es igual a 10
    print("Se ejecuta la condicion del segundo if")
else: print("Se ejecuta la condicion del else porque no es 10")

if mi_condicional > 10 : #si mi condicion es mayor a 10
    print("Es mayor a 10")
else: 
    print("Es menor o igual a 10")
    
if mi_condicional > 10 and mi_condicional < 20: #si mi condicion es mayor a 10 y menor a 20
    print("Es mayor que 10 y menor que 20")
else: print("Es menor o igual a 10 o mayor o igual a 20")

# if, elif, else

if mi_condicional > 10 and mi_condicional < 20 :
    print("Es mayor que 10 y menor que 20")
elif mi_condicional == 0:
    print("Es igual a 0")
else:
    print("Es menor o igual a 10 o mayor o igual a 20")
    
    
# Condicional con ispección de valor

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")
