from Datos import *
from Funciones import *


def jugar():
    imprimir_tablero(tablero)
    mover_pieza()

    print("Se ha terminado el juego:")
    if not negras[4] in tablero:
        print("¡Ganan las blancas!")
    elif not blancas[4] in tablero:
        print("¡Ganan las negras!")

def volver_a_jugar():
    while True:
        respuesta = input("¿Quieres volver a jugar? (si/no) ")
        if respuesta == "si":
            print("¡Vamos a jugar otra vez! \n")
            return jugar()
        elif respuesta == "no":
            return False
        else:
            print("No has introducido una opción válida. Prueba otra vez.")

jugar()
volver_a_jugar()
