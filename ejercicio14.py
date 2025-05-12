#Contar vocales
#Escribe una función que reciba una cadena y devuelva la cantidad de vocales.
#¿Qué hace for letra in cadena:?
#Significa: "mira una por una cada letra del texto".
#Ejemplo con "Hola":
#Primero ve "H"
#Luego "o"
#Luego "l"
#Luego "a"
#Y va revisando si es una vocal o no.

def vocales(cadena):
    # Hacemos una lista con todas las vocales que queremos contar
    vocales = "Amando y conociendo es que cumplo cada uno de mis sueños"
    # Creamos un contador que empieza en 0
    contador = 0

    # Recorremos cada letra de la cadena
    for letra in cadena:
        # Si la letra está dentro del grupo de vocales...
        if letra in vocales:
            contador += 1  # ...aumentamos el contador en 1

    # Al final, devolvemos cuántas vocales encontramos
    return contador

# Probamos la función
texto = "Mariana"
print(vocales(texto))  # Imprime: 5


