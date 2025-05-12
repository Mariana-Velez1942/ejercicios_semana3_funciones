#Generador de contraseñas
#Crea una función que genere una contraseña aleatoria de una longitud dada.

import random  # Necesitamos esta herramienta para elegir cosas al azar
import string  # Este módulo contiene las letras y los números

# Función para generar una contraseña aleatoria
def generar_contraseña(longitud):
    # Combinamos letras minúsculas, mayúsculas, números y símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Elegimos caracteres al azar de esa combinación, tantas veces como longitud indiquemos
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

    return contraseña  # Devolvemos la contraseña generada

# Usamos la función para generar una contraseña de 12 caracteres (puedes cambiar el número)
longitud_deseada = 12
contraseña_generada = generar_contraseña(longitud_deseada)

print("Contraseña generada:", contraseña_generada)
