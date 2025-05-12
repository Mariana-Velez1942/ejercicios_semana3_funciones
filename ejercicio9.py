#Filtrar pares
#Crea una función que reciba una lista de números y devuelva solo los pares.

def pares(lista):
    pares=[]
    for numeros in lista:
        if numeros % 2 == 0:
            pares.append(numeros)
            return pares
print(pares([2,5,]))
