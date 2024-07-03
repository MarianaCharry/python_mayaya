#En un archivo llamado twttr.py, implementa un programa que solicite al usuario una cadena de texto y luego muestre esa misma cadena de texto,
#pero sin todas las vocales (A, E, I, O y U), ya sea que hayan sido ingresadas en mayúsculas o minúsculas.

def no_vocales(cadena):
    vocales = 'aeiouAEIOU'
    resultado = ''.join([letra for letra in cadena if letra not in vocales])
    return resultado

texto=input("Ingrese un mensaje ")

resultado = no_vocales(texto)
print("Mensaje completo: ")
print(texto)
print("Mensaje sin vocales: ")
print(resultado)


