#Composición de funciones
#Escribe una función que reciba otra función como parámetro y aplique una composición de funciones.

# Definimos dos funciones simples
def multiplicar_por_2(x):
    return x * 2

def sumar_3(x):
    return x + 3

#  creamos una función que reciba otra función como parámetro
def componer_funciones(func1, func2, valor):
    # Aplicamos func1 primero, luego func2 sobre el resultado de func1
    return func2(func1(valor))

#  probamos nuestra composición con las funciones que definimos antes
resultado = componer_funciones(multiplicar_por_2, sumar_3, 5)  # Componer las funciones con el valor 5
print("El resultado de la composición es:", resultado)
