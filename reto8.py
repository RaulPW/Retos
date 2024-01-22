import re
import unidecode

"""/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 * - Heterograma: es una palabra o frase que no contiene ninguna letra repetida.
 * - Isograma: es una palabra o frase en la que cada letra aparece el mismo número de veces.
 * - Pangrama: frase en la que aparecen todas las letras del abecedario.
 
 /"""

def contar_letras(texto):


    texto_sin_acento = unidecode.unidecode(texto.lower())
    texto_limpio = re.sub(r'\s', '', texto_sin_acento)
    contar_letras = dict()
    
    for letra in texto_limpio:
        if letra in contar_letras.keys():
            contar_letras[letra] += 1
        else:
            contar_letras[letra] = 1

    return contar_letras





def is_heterograma(texto):
    for contador in contar_letras(texto).values():
        if contador > 1:
            return False
    return True
    
def is_isograma(texto):
    order = 0
    for contador in contar_letras(texto).values():
        if order == 0:
            order = contador
        if order != contador:
            return False

    return True

    
def is_pangrama(texto):
    return len(contar_letras(texto).keys()) == 27

if __name__ == "__main__":

    frase = input("Escriba una frase: ")
    if is_heterograma(frase):
        print("Esta frase un heterograma")
    elif is_isograma(frase):
        print("Esya frase es un isograma")
    elif is_pangrama(frase):
        print("Esta frase es un pangrama")
    else:
        print("Esta frase no es pertenece a ninguna clase anterior")