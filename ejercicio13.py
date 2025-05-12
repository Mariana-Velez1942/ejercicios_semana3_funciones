#FizzBuzz
#Crea una función que reciba un número y devuelva "Fizz", "Buzz" o "FizzBuzz" según las reglas del juego.

def juego(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero  # Devuelve el número si no cumple ninguna condición

# Probamos con el número 15
print(juego(15))  # Esto imprimirá: FizzBuzz
