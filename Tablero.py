from Datos import *
from Funciones import *


def jugar():
    imprimir_tablero(tablero)
    while negras[4] or blancas[4] in tablero:
        mover_pieza()
        break

    print("Se ha terminado el juego:")
    if not negras[4] in tablero:
        print("¡Ganan las blancas!")
    elif not blancas[4] in tablero:
        print("¡Ganan las negras!")

jugar()
