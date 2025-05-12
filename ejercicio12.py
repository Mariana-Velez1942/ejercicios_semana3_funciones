#Eliminar duplicados
#Escribe una función que reciba una lista y devuelva una nueva sin elementos repetidos.

# 1 hacemos la lista

def eliminar_duplicados(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

numeros = [3, 1, 2, 3, 4, 2, 5]
print(eliminar_duplicados(numeros))  # Resultado: [3, 1, 2, 4, 5]
#es un método de lista que sirve para añadir un nuevo elemento al final de una lista existente. Este elemento puede ser de cualquier tipo de dato, incluyendo otras listas, cadenas, números, u otros objetos. 

#Un set (conjunto) es una estructura que no permite elementos repetidos.
#Por ejemplo: set([1, 2, 2, 3]) se convierte en {1, 2, 3}.
#list(set(lista)):
#Convertimos el conjunto de nuevo a lista, porque set no tiene orden ni soporta indexado.