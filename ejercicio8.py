#Contar letras
#Escribe una función que cuente cuántas veces aparece una letra en una palabra.

def contar_letra(palabra, letra):
    # Convierte todo a minúsculas para que la comparación sea justa
    palabra = palabra.lower()
    letra = letra.lower()
    
    # Cuenta cuántas veces aparece la letra en la palabra
    return palabra.count(letra)

# Pedimos los datos al usuario
palabra_usuario = input("Escribe una palabra: ")
letra_usuario = input("Escribe la letra que quieres contar: ")

# Validamos que el usuario solo haya escrito una letra
if len(letra_usuario) != 1:
    print("Por favor, escribe solo una letra.")
else:
    resultado = contar_letra(palabra_usuario, letra_usuario)
    print(f"La letra '{letra_usuario}' aparece {resultado} veces en la palabra '{palabra_usuario}'.")
