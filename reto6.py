"""/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */"""

p1 = """¿Cuáles de los siguientes adjetivos odiarías más que te digan los otros?
        \n1.- Cobarde\n2.- Ordinario\n3.- Egoista\n4.- Ignorante"""

p2 = """Una vez cada siglo, el arbusto Flutterby produce flores que adoptan su aroma para atraer a los incautos. Si este te llegase a atraer, tu olerias:\n1.- Un fuego de leña crepitante\n2.- El mar\n3.- El aroma de tu hogar\n4.- Pergamino fresco"""

p3 = "Dada la elección, preferirías inventar una poción que te garantizara:\n1.- Gloria\n2.-Poder\n3.- Amor\n4.- Sabiduria"

p4 = """Después de que hayas muerto, ¿qué es lo que más te gustaría que hicieran los demás cuando escuchen tu nombre?\n1.- Que pidan más historias de tus aventuras\n2.- No me importa lo que la gente piense de mí mientras estoy muerto; es lo que piensen de mí mientras vivo lo que cuenta\n3.- Lo/la extraño, esa persona sonríe\n4.- Piensen con admiración tus logros"""

p5 = """¿Qué tipo de instrumento le agrada más a tu oído?\n1.- El tambor\n2.- El violin\n3.- La trompeta\n4.- El piano"""

p6 = """¿Cuál camino te tienta más?\n1.- El camino retorcido y cubierto de hojas a través del bosque\n2.- El callejon estrecho, oscuro, iluminado por las linternas\n3.- El carril ancho, soleado y hierboso\n4.- La calle empedrada llena de edificios antiguos"""

listado_pr = (p1, p2, p3, p4, p5, p6)

dict_resultado = {"grifindor": 0, 'slytherin' : 0, 'hufflepuff' : 0, 'ravenclaw' : 0}


for pregunta in listado_pr:
    print(pregunta)
    respuesta = int(input("\nPor favor, escoja una respuesta: "))
    if respuesta == 1:
        dict_resultado['grifindor'] += 1
    elif respuesta == 2:
        dict_resultado['slytherin'] += 1
    elif respuesta == 3:
        dict_resultado['hufflepuff']+= 1
    elif respuesta == 4:
        dict_resultado['ravenclaw'] += 1
    else:
        print("Debe indicar una respuesta válida")

print(f"Te envio a la casa {(max(dict_resultado, key=dict_resultado.get)).title()}")

