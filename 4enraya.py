def crear_tablero(filas, columnas):
    tablero=[]
    for fila in range(filas):
        tablero.append([' ']*columnas)
    return tablero
    
    
def imprimir_tablero(tablero):
    for fila in range(len(tablero)):
        print(fila,'|', end='')
        for columna in range(len(tablero[0])):
            print(tablero[fila][columna] + '|', end='')
        print()
    print('-' * len(tablero[0]) * 2 + '-')
    
'''
Función que pide al usuario una columna para ver si en esa columna puede meter la ficha
La función devolverá una coordenada (x,y) donde se pondrá la ficha del jugador correspondiente
'''
def pedir_jugada(jugador,tablero):
    columnaAJugar = int(input("Jugador: '"+str(jugador)+"' elige una columna del 0-"+ str(len(tablero[0])-1)))
    filaAJugar= len(tablero)
    for jugada in range(filaAJugar):
        filaAJugar -= 1
        if tablero[filaAJugar][columnaAJugar] == " ":
            return filaAJugar,columnaAJugar
    print("Fila llena, vuelve a intentarlo")
    return pedir_jugada(jugador,tablero)
    

'''
En la función jugar(función principal del juego) crearemos el tablero, los jugadores
y pediremos las jugadas al jugador correspondiente
'''
def jugar():
    tablero = crear_tablero(6,7)
    jugadores = ["X","O"]
    turno = 1
    imprimir_tablero(tablero)
    while turno != len(tablero) * len(tablero[0]):
        jugadorActual=""
        if turno % 2 == 0:
            jugadorActual=jugadores[1]
        else:
            jugadorActual=jugadores[0]
        fila,columna = pedir_jugada(jugadorActual,tablero)
        tablero[fila][columna] = jugadorActual
        imprimir_tablero(tablero)
        turno+=1
        if comprobarJugada(tablero,jugadorActual):
            print("Ha ganado el jugador", jugadorActual)
        else:
            print("La pratida es empate")
            break
            

'''
Función que devuelve un True o False en función de si la jugada ha completado un
4 en raya
Para comprobar este 4 en raya hay que ver si ha hecho una:
    - Vertical
    - Horizontal
    - Diagonal hacia la derecha
    - Diagonal hacia la izquierda
'''
def comprobarJugada(tablero, jugadorActual):
    # Comprobar vertical
    for columna in range(len(tablero[0])):
        for fila in range(len(tablero)-3):
            if tablero[fila][columna] == jugadorActual and tablero[fila+1][columna] == jugadorActual and tablero[fila+2][columna] == jugadorActual and tablero[fila+3][columna] == jugadorActual:
                return True
    
    # Comprobar horizontal
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])-3):
            if tablero[fila][columna] == jugadorActual and tablero[fila][columna+1] == jugadorActual and tablero[fila][columna+2] == jugadorActual and tablero[fila][columna+3] == jugadorActual:
                return True
    
    # Comprobar diagonal hacia la derecha
    for fila in range(len(tablero)-3):
        for columna in range(len(tablero[0])-3):
            if tablero[fila][columna] == jugadorActual and tablero[fila+1][columna+1] == jugadorActual and tablero[fila+2][columna+2] == jugadorActual and tablero[fila+3][columna+3] == jugadorActual:
                return True
    
    # Comprobar diagonal hacia la izquierda
    for fila in range(len(tablero)-3):
        for columna in range(3, len(tablero[0])):
            if tablero[fila][columna] == jugadorActual and tablero[fila+1][columna-1] == jugadorActual and tablero[fila+2][columna-2] == jugadorActual and tablero[fila+3][columna-3] == jugadorActual:
                return True
    
    return False

imprimir_tablero(crear_tablero(6,7))
pedir_jugada("X",crear_tablero(6,7))
jugar()
#print(pedir_jugada("X",crear_tablero(6,7)))

