

tablero = [['♜',	'♞',	'♝',	'♛',   '♚', 	'♝', 	'♞', 	'♜'],
           ['♟',	'♟',	'♟',	'♟',   '♟', 	'♟', 	'♟', 	'♟'],
           [' ',	 ' ',     ' ',     ' ',    ' ', 	 ' ', 	 ' ', 	  ' '],
           [' ',	 ' ',	  ' ',	   ' ',    ' ', 	 ' ', 	 ' ', 	  ' '],
           [' ',	 ' ',	  ' ',	   ' ',    ' ', 	 ' ', 	 ' ', 	  ' '],
           [' ',	 ' ',	  ' ',	   ' ',    ' ', 	 ' ', 	 ' ', 	  ' '],
           ['♙',	'♙',	'♙',	'♙',   '♙', 	'♙', 	'♙', 	'♙'],
           ['♖',	'♘',	'♗',	'♕',   '♔', 	'♗', 	'♘', 	'♖']
          ]


negras = ['♜', '♞', '♝', '♛', '♚', '♝',	'♞', '♜', '♟', '♟',	'♟', '♟', '♟', '♟', '♟', '♟']
blancas = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']

def imprimir_tablero(tablero):
    print("    A B C D E F G H")
    print("  + ――—―—―—―—―—―—―—―—")
    
    for i in range(8): 
        print(i+1, "|", end = " ")
        for j in range(8):
            print(tablero[i][j], end = " ")
        print()
    print("\n")
        
imprimir_tablero(tablero)


def quieres_jugar():
    respuesta = input("¿Quieres jugar? (si/no): ")
    if respuesta == "si":
        print("Dale pa, juega.")
    elif respuesta == "no":
        print("Se acabó el juego. :(")
        print("Este es tu tablero: \n")
        print(imprimir_tablero(tablero))

quieres_jugar()

def movimientos():
    print("¿Qué pieza quieres mover?")
    pieza = input()
    if pieza in negras:
        print("Es una pieza negra. \n")
    elif pieza in blancas:
        print("Es una pieza blanca. \n")
    else:
        print("No hay ninguna pieza en esa posición. \n")

movimientos()

def mover_pieza():
    print("¿A qué posición quieres mover la pieza?")
    posicion = input()
    if posicion in tablero:
        print("Hay una pieza en esa posición. \n")
    else:
        print("No hay ninguna pieza en esa posición. \n")

mover_pieza()