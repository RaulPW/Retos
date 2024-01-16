"""/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */"""

# Vamos a definir para cada elemento una funcion donde se pasará por parámetro el elemento escogido por el player 2
# de tal manera que devuelva quien ha ganado esa jugada.

def is_piedra(elemento):
    if elemento == "lagarto" or elemento == "tijeras":
        return True
    elif elemento == "papel" or elemento == "spock":
        return False
    
def is_papel(elemento):
    if elemento == "piedra" or elemento == "spock":
        return True
    elif elemento == "tijeras" or elemento == "lagarto":
        return False
    
def is_tijera(elemento):
    if elemento == "lagarto" or elemento == "papel":
        return True
    elif elemento == "piedra" or elemento == "spock":
        return False

def is_lagarto(elemento):
    if elemento == "spock" or elemento == "papel":
        return True
    elif elemento == "piedra" or elemento == "tijeras":
        return False

def is_spock(elemento):
    if elemento == "piedra" or elemento == "tijeras":
        return True
    elif elemento == "papel" or elemento == "lagarto":
        return False
    

if __name__ == "__main__":

    p1 = 0
    p2 = 0

    entrada_partida = [("piedra", "tijeras"), ("papel", "spock"), ("lagarto", "tijeras"), ("spock", "papel"), ("piedra", "lagarto")]

    #creamos bucle for para recorrer la partida y determinar quien gana en cada jugada.

    for jugada in entrada_partida:
        if jugada[0] == "piedra":
            if is_piedra(jugada[1]) == True:
                p1 += 1
            else:
                p2 += 1
        if jugada[0] == "tijera":
            if is_tijera(jugada[1]) == True:
                p1 += 1
            else:
                p2 += 1
        if jugada[0] == "papel":
            if is_papel(jugada[1]) == True:
                p1 += 1
            else:
                p2 += 1
        if jugada[0] == "lagarto":
            if is_lagarto(jugada[1]) == True:
                p1 += 1
            else:
                p2 += 1
        if jugada[0] == "spock":
            if is_spock(jugada[1]) == True:
                p1 += 1
            else:
                p2 += 1


    
    # Comparamos los resultados de ambos jugadores e indicamos quien ha ganado:
    if p1 == p2:
        print("Empate")
    elif p1 > p2:
        print("Player 1")
    else:
        print("Player2")
