# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta                                 Tipo Impositivo
#Menos de $10000                            5%
#Entre $10000 y $20000                      15%
#Entre $20000 y $35000                      20%
#Entre $35000 y $60000                      30%
#Mas de $60000                              45%

#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo 
# que le corresponde

# Preguntar al usuario por la renta
renta = float(input("Ingrese el valor de su renta anual: "))
## Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta <35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
#Mostramos en pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ",renta*tipo /100, "$", sep='')
    