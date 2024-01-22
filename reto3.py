import random
import string

"""/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */"""

def generar_password(longitud, mayuscula = True, minuscula = True, numeros = True, simbolos = True):
    caracteres = ""
    if longitud < 8 or longitud > 16:
        print("Debe indicar un número entre 8 y 16")
    else:
        if mayuscula:
            caracteres += string.ascii_uppercase
        if minuscula:
            caracteres += string.ascii_lowercase
        if numeros:
            caracteres += string.digits
        if simbolos:
            caracteres += string.punctuation

    
    password = ""
    for i in range(longitud):
        password += random.choice(caracteres)
    return password

#generar_password(20)
password = generar_password(13)
print(password)



