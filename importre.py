import re
import unidecode

frase = "Esto es una prueba para ver si aprendo algo de la libreria re"

quitar_espacios = re.sub(r"\s", "", frase)
                         
print(quitar_espacios)

uni = "Voy a escribir mi nombre con acento Raúl, además más acentos por aquí"

palabra_sin_acento = unidecode.unidecode(uni)
print(palabra_sin_acento)