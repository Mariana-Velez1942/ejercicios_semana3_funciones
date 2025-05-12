#Mayoría de edad
#Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.

def mayor_o_menor(edades):
    if edades < 18:
        return "Eres menor de edad"
    else:
        return "Eres mayor de edad"
print(mayor_o_menor(2))
print(mayor_o_menor(50))