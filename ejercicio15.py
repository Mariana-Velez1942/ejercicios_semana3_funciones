#Invertir texto
#Crea una función que invierta una cadena de texto.

# Creamos una función que se llama invertir_texto
def invertir_texto(texto):
    # Esta línea invierte el texto usando slicing [::-1]
    texto_invertido = texto[::-1]

    # Devolvemos (return) el texto invertido
    return texto_invertido

# Pedimos al usuario que escriba una frase o palabra
entrada = input("Escribe una palabra: ")

# Llamamos a la función y guardamos el resultado
resultado = invertir_texto(entrada)

# Mostramos el resultado
print("Texto invertido:", resultado)
