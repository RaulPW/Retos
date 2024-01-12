"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */"""



diccionario = {
    
        'a': '4', 'b': '8', 'c': '(', 'd': 'd', 'e': '3', 'f': 'f', 'g': '9',
        'h': '#', 'i': '1', 'j': 'j', 'k': 'k', 'l': '1', 'm': 'm', 'n': 'n',
        'o': '0', 'p': 'p', 'q': 'q', 'r': '2', 's': '5', 't': '7', 'u': 'u',
        'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': '2', '0': '0', '1': '1',
        '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
        '9': '9'
    
}

texto = "Quiero transformar estas palabras a texto hacker"
texto_hacker = ""
"""for letra in texto:
    for clave, valor in diccionario.items():
        if letra.upper() == clave:
            texto_hacker += valor
            break     
        elif letra == " ":
            texto_hacker += letra
            break

print(texto_hacker)

for i in range (len(texto)):
    if texto[i].upper() in diccionario:
        texto_hacker += diccionario[texto[i].upper()]
    else:
        texto_hacker += texto[i]

print("Otro modo de solucionarlo", texto_hacker)"""


def traductor(texto):
    dict_1 = {
        "a": "4",
        "b": "I3",
        "c": "[",
        "d": ")",
        "e": "3",
        "f": "|=",
        "g": "&",
        "h": "#",
        "i": "1",
        "j": ",_|",
        "k": "|<",
        "l": "|",
        "m": "[v]",
        "n": "^/",
        "o": "0",
        "p": "?",
        "q": "9",
        "r": "2",
        "s": "5",
        "t": "7",
        "u": "(_)",
        "v": "\/",
        "w": "N/",
        "x": "><",
        "y": "\|/",
        "z": "%",
        " ":" "
    }
    resultado = ""
    for i in texto:
        resultado += dict_1[i.lower()]
    return resultado


entrada = input("El texto: ")
texto_nuevo = traductor(entrada)
print(texto_nuevo)




