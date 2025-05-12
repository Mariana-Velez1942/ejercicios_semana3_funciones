#Factorial
#Crea una función que calcule el factorial de un número entero positivo.

def numero_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * numero_factorial(n-1)
print(numero_factorial(10))