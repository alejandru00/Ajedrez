

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
    print("   ――—―—―—―—―—―—―—―—")
    
    for i in range(8): 
        print(i+1, "|", end = " ")
        for j in range(8):
            print(tablero[i][j], end = " ")
        print()
    print("\n")
        
imprimir_tablero(tablero)


def mover_pieza():
    fila_origen = input('Introduce la fila de la pieza a mover: ')
            
    input('Introduce la columna de la pieza a mover: ')
    columna_origen = int()
    input('Introduce la fila de destino: ')
    fila_destino = int()
    input('Introduce la columna de destino: ')
    columna_destino = int()
    
    tablero[fila_origen][fila_destino] = tablero[columna_origen][columna_destino]
    tablero[columna_origen][columna_destino] = ' '
    print(imprimir_tablero(tablero))
    


mover_pieza()