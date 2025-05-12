#Mayor de una lista
#Crea una función que reciba una lista de números y devuelva el mayor.

def numero_mayor(numeros):
    return max (numeros) # el max es un iterable
lista =[2,5,8,9,4,45,23] # se crea la lista
mayor = numero_mayor(lista) # llamamos la lista
print("El numero mayor es",mayor) 
