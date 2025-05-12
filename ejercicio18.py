#Suma de elementos únicos
#Escribe una función que reciba una lista de números y devuelva la suma de los elementos únicos.

# Creamos una lista de números 
numeros = [1, 2, 3, 2, 1, 4]

# usamis una función muy sencilla
def sumar_unicos(lista):
    suma = 0  # Aquí guardamos la suma total (empezamos desde cero)

    for numero in lista:  # Recorremos cada número de la lista
        if lista.count(numero) == 1:  # Si ese número solo aparece una sola vez
            suma += numero  # Lo sumamos

    return suma  # Cuando terminamos, devolvemos el total

# Llamamos la función y mostramos el resultado
resultado = sumar_unicos(numeros)
print("La suma de los elementos únicos es:", resultado)


