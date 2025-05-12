#Conversor de temperatura
#Crea una función que convierta grados Celsius a Fahrenheit.
# formula para la conversion F = C × 9/5 + 32

def celsius_a_farenheit(celcius):
    farenheit = celcius * 9 / 5 + 32
    return farenheit
print(celsius_a_farenheit(23.5))