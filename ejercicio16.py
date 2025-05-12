#Validar contraseña segura
#Escribe una función que valide si una contraseña cumple con requisitos de seguridad
#  (mayúsculas, minúsculas, números y símbolos).


# Creamos una función para revisar si una contraseña es segura
def validar_contraseña(contraseña):
    # Creamos 4 banderas para saber si tiene los elementos necesarios
    tiene_mayuscula = False  # Aún no sabemos si tiene letra grande
    tiene_minuscula = False  # Aún no sabemos si tiene letra pequeña
    tiene_numero = False     # Aún no sabemos si tiene número
    tiene_simbolo = False    # Aún no sabemos si tiene símbolo

    # Vamos a mirar letra por letra en la contraseña
    for caracter in contraseña:
        if caracter.isupper():  # ¿Es letra mayúscula?
            tiene_mayuscula = True
        elif caracter.islower():  # ¿Es letra minúscula?
            tiene_minuscula = True
        elif caracter.isdigit():  # ¿Es un número?
            tiene_numero = True
        else:
            # Si no es letra ni número, entonces es un símbolo
            tiene_simbolo = True

    # Ahora revisamos si tiene  lo necesario
    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo:
        return "¡Contraseña segura!"
    else:
        return " Contraseña débil. Usa mayúsculas, minúsculas, números y símbolos."

# Pedimos al usuario que escriba una contraseña
clave = input("Escribe una contraseña para revisarla: ")

# Llamamos a la función y mostramos el resultado
print(validar_contraseña(clave))
