#Palíndromo
#Escribe una función que determine si un texto es un palíndromo.

def texto_palindromo(cadena):
    return cadena == cadena[::-1] #Esta línea normalmente se usa en una función que verifica si una palabra o frase es un palíndromo, es decir, que se lee igual al derecho que al revés (como "oso", "ana", "reconocer").
print(texto_palindromo("radar")) 
print(texto_palindromo("ama")) 
print(texto_palindromo("Amo la paloma")) 
