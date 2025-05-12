#Simular dado
#Crea una función que simule el lanzamiento de un dado de 6 caras.

# Importamos una caja de herramientas llamada "random"
# Esta nos deja hacer cosas al azar, como lanzar un dado
import random

# Creamos una función que simula lanzar un dado
def lanzar_dado():
    # Elegimos un número al azar entre 1 y 6
    resultado = random.randint(1, 6)
    return resultado  # Devolvemos el número que salió

# Ahora le decimos al usuario que vamos a lanzar el dado
input("Presiona Enter para lanzar el dado... 🎲")

# Llamamos a la función para lanzar el dado
numero = lanzar_dado()

# Mostramos el número que salió en pantalla
print(f"¡Salió el número {numero}!")
