from Datos import *

def imprimir_tablero(tablero):          #printeo el tablero con el nombre de las filas y columnas.
    print("    A B C D E F G H")        
    print("  + ――—―—―—―—―—―—―—―—")
    
    for i in range(8): 
        print(i+1, "|", end = " ")
        for j in range(8):
            print(tablero[i][j], end = " ")
        print()
    print("\n")


def mover_pieza():
    guardar_archivo = input("Esta partida va a guardarse en un archivo. ¿Cómo quieres que se llame este? ")      #Pregunto el nombre el archivo donde voy a guardar las jugadas.

    if negras[4] or blancas[4] in tablero:                                           #Mientras el rey de cada bando esté en el tablero, el juego sigue.
        
        f = open(guardar_archivo, "w")                                                  #Creo el archivo donde voy a guardar las jugadas.

        while True:
            fila_inicio = int(input("Introduce la fila de la pieza a mover: "))         #Pido la fila y columna de la pieza a mover
            if fila_inicio == 1:                                                        #... y hago mas intuitivo el input para el jugador
                fila_inicio = 0                                                         #... ya que en el tablero las filas empiezan en 0 y no en 1.
                break
            elif fila_inicio == 2:
                fila_inicio = 1
                break
            elif fila_inicio == 3:
                fila_inicio = 2
                break
            elif fila_inicio == 4:
                fila_inicio = 3
                break
            elif fila_inicio == 5:
                fila_inicio = 4
                break
            elif fila_inicio == 6:
                fila_inicio = 5
                break
            elif fila_inicio == 7:
                fila_inicio = 6
                break
            elif fila_inicio == 8:
                fila_inicio = 7
                break
            else:
                print("Esa fila no existe, pruebe otra vez.")

        while True:
            columna_inicio = input("Introduce la columna de la pieza a mover: ")        #Pido la columna de la pieza a mover
            if columna_inicio == "A":                                                   #... y hago mas intuitivo el input para el jugador
                columna_inicio = 0                                                      #... ya que en el tablero las columnas empiezan en 0 y no en A.
                break
            elif columna_inicio == "B":
                columna_inicio = 1
                break
            elif columna_inicio == "C":
                columna_inicio = 2
                break
            elif columna_inicio == "D":
                columna_inicio = 3
                break
            elif columna_inicio == "E":
                columna_inicio = 4
                break
            elif columna_inicio == "F":
                columna_inicio = 5
                break
            elif columna_inicio == "G":
                columna_inicio = 6
                break
            elif columna_inicio == "H":
                columna_inicio = 7
                break
            else:
                print("Esa columna no existe, pruebe otra vez.")
                

        if tablero[fila_inicio][columna_inicio] in negras:                     #Comunico al jugador que tipo de pieza que ha seleccionado.
            print("Es una pieza negra. \n")
        elif tablero[fila_inicio][columna_inicio] in blancas:
            print("Es una pieza blanca. \n")
        else:
            print("No hay ninguna pieza en esa posición. Vuelve a intentarlo. \n")      #Si no hay ninguna pieza en esa posición, vuelve a pedir la posición de la pieza a mover.
            return mover_pieza()

        while True:
            fila_final = int(input("Introduce la fila de destino: "))           #Pido la fila y columna de destino
            if fila_final == 1:                                                 #... y hago mas intuitivo el input para el jugador
                fila_final = 0                                                  #... ya que en el tablero las filas empiezan en 0 y no en 1.
                break
            elif fila_final == 2:
                fila_final = 1
                break
            elif fila_final == 3:
                fila_final = 2
                break
            elif fila_final == 4:
                fila_final = 3
                break
            elif fila_final == 5:
                fila_final = 4
                break
            elif fila_final == 6:
                fila_final = 5
                break
            elif fila_final == 7:
                fila_final = 6
                break
            elif fila_final == 8:
                fila_final = 7
                break
            else:
                print("Esa fila no existe, pruebe otra vez.")
                

        while True:
            columna_final = input("Introduce la columna de destino: ")        #Pido la columna de destino
            if columna_final == "A":                                          #... y hago mas intuitivo el input para el jugador              
                columna_final = 0                                             #... ya que en el tablero las columnas empiezan en 0 y no en A.
                break
            elif columna_final == "B":
                columna_final = 1
                break
            elif columna_final == "C":
                columna_final = 2
                break
            elif columna_final == "D":
                columna_final = 3
                break
            elif columna_final == "E":
                columna_final = 4
                break
            elif columna_final == "F":
                columna_final = 5
                break
            elif columna_final == "G":
                columna_final = 6
                break
            elif columna_final == "H":
                columna_final = 7
                break
            else:
                print("Esa columna no existe, pruebe otra vez.")

        if tablero[fila_final][columna_final] in tablero:                       #Compruebo si hay una pieza en la posición de destino.
            print("Hay una pieza en esa posición. \n")
            if tablero[fila_final][columna_final] in negras and tablero[fila_inicio][columna_inicio] in negras:
                print("No puedes comer una pieza de tu mismo color. \n")        #Y en el caso de que sea del mismo color que la pieza que se quiere mover, 
                return mover_pieza                                              #... no permito el movimiento y hago repetirlo.
            else:
                print("Has comido una pieza. \n")                               #En el caso de que sea del color contrario, permito el movimiento.

        else:
            print("No hay ninguna pieza en esa posición. \n")

        
        tablero[fila_final][columna_final] = tablero[fila_inicio][columna_inicio]   #Muevo la pieza de la posición de inicio a la de destino.
        tablero[fila_inicio][columna_inicio] = " "                                  #... y vacío la posición de inicio.
        print(imprimir_tablero(tablero))                                            #Imprimo el tablero con la pieza movida.                  

    
        f.write(f"{imprimir_tablero(tablero)}")                                     #Guardo el movimiento (nuevo tablero) en el archivo de texto.                 
        f.close()

    else: 
        pass




