#Número par o impar
#Crea una función que determine si un número es par o impar.

def par_o_impar(numero):
    if numero % 2 ==0:
        return("Es par")
    else:
        return ("Es impar")

print(par_o_impar(2))
print(par_o_impar(7))