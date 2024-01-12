"""*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */"""





def partido(secuencia):
    puntos_actual_p1 = "Love"
    puntos_actual_p2 = "Love"
    puntuaciones = ["Love", 15, 30, 40, 'Ventaja']
    for player in secuencia:
        if player == "P1":
            for i in range(len(puntuaciones)):
                if puntos_actual_p1 == "Ventaja" and puntos_actual_p2 == 40:
                    puntos_actual_p1 = "win"
                elif puntos_actual_p1 == puntuaciones[i]:
                    puntos_actual_p1 = puntuaciones[i+1]
                    break
        if player == "P2":
            for i in range(len(puntuaciones)):
                if puntos_actual_p2 == "Ventaja" and puntos_actual_p1 == 40:
                    puntos_actual_p2 = "win"
                elif puntos_actual_p2 == puntuaciones[i]:
                    puntos_actual_p2 = puntuaciones[i+1]
                    break
    if puntos_actual_p1 == "win":
        print("Ha ganado el P1")
    elif puntos_actual_p2 == "win":
        print("Ha ganado el P2")
    elif puntos_actual_p1 == 40 and puntos_actual_p2 == 40:
        print("Deuce")
    else:
        print(f"{puntos_actual_p1} - {puntos_actual_p2}")

if __name__ == "__main__":
    secuencia_puntos1 = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
    secuencia_puntos2 = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P2', 'P2']

    partido(secuencia_puntos1)
    partido(secuencia_puntos2)

    
