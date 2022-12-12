from Datos import *

def imprimir_tablero(tablero):
    print("    A B C D E F G H")
    print("   ――—―—―—―—―—―—―—―—")
    
    for i in range(8): 
        print(i+1, "|", end = " ")
        for j in range(8):
            print(tablero[i][j], end = " ")
        print()
    print("\n")

def mover_pieza():
    if input == ("A", "B", "C", "D", "E", "F", "G", "H"):
        columna_inicio = (0, 1, 2, 3, 4, 5, 6, 7)

    else:
        print("No es una columna válida. Vuelve a intentarlo. \n")
        return mover_pieza

    fila_inicio = int(input("Introduce la fila de la pieza a mover: "))
    columna_inicio = int(input("Introduce la columna de la pieza a mover: "))

    if tablero[fila_inicio][columna_inicio] in negras:
        print("Es una pieza negra. \n")
    elif tablero[fila_inicio][columna_inicio] in blancas:
        print("Es una pieza blanca. \n")
    else:
        print("No hay ninguna pieza en esa posición. Vuelve a intentarlo. \n")
        return mover_pieza


    fila_final = int(input("Introduce la fila de destino: "))
    columna_final = int(input("Introduce la columna de destino: "))

    if tablero[fila_final][columna_final] in tablero:
        print("Hay una pieza en esa posición. \n")
        if tablero[fila_final][columna_final] in negras and tablero[fila_inicio][columna_inicio] in negras:
            print("No puedes comer una pieza de tu mismo color. \n")
            return mover_pieza
        else:
            print("Has comido una pieza. \n")

    else:
        print("No hay ninguna pieza en esa posición. \n")

     
    tablero[fila_final][columna_final] = tablero[fila_inicio][columna_inicio] 
    tablero[fila_inicio][columna_inicio] = " "
    print(imprimir_tablero(tablero))

