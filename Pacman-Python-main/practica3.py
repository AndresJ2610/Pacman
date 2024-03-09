import random

Tablero = []
x = 17
y = 42

for i in range(x):
    Tablero.append([])
    for j in range(y):
        Tablero[i].append(" ")

for i in range(1):
    for j in range(y):
        Tablero[i][j] = "#"
for i in range(16,17):
    for j in range(y):
        Tablero[i][j] = "#"
for i in range(x):
    for j in range(1):
        Tablero[i][j] = "#"
for i in range(x):
    for j in range(41,42):
        Tablero[i][j] = "#"

Tablero[2][4] = "═"
Tablero[2][5] = "═"
Tablero[2][6] = "═"
Tablero[2][7] = "═"
Tablero[2][8] = "═"
Tablero[2][9] = "═"
Tablero[2][10] = "═"
Tablero[2][11] = "═"
Tablero[2][18] = "═"
Tablero[2][19] = "═"
Tablero[2][20] = "═"
Tablero[2][21] = "═"
Tablero[2][22] = "═"
Tablero[2][23] = "═"
Tablero[2][24] = "═"
Tablero[2][25] = "═"
Tablero[2][26] = "═"
Tablero[2][32] = "═"
Tablero[2][33] = "═"
Tablero[2][34] = "═"
Tablero[2][35] = "═"
Tablero[2][36] = "═"
Tablero[2][37] = "═"
Tablero[2][38] = "═"
Tablero[3][4] = "║"
Tablero[3][22] = "║"
Tablero[3][38] = "║"
Tablero[4][4] = "║"
Tablero[4][38] = "║"
Tablero[5][4] = "║"
Tablero[5][38] = "║"
Tablero[6][4] = "║"
Tablero[6][38] = "║"
Tablero[7][4] = "║"
Tablero[7][38] = "║"
Tablero[9][12] = "═"
Tablero[9][13] = "═"
Tablero[9][14] = "═"
Tablero[9][18] = "═"
Tablero[9][19] = "═"
Tablero[9][20] = "═"
Tablero[9][21] = "═"
Tablero[9][23] = "═"
Tablero[9][24] = "═"
Tablero[9][25] = "═"
Tablero[9][26] = "═"
Tablero[9][30] = "═"
Tablero[9][31] = "═"
Tablero[9][32] = "═"
Tablero[11][4] = "║"
Tablero[11][38] = "║"
Tablero[12][4] = "║"
Tablero[12][38] = "║"
Tablero[13][4] = "║"
Tablero[13][22] = "║"
Tablero[13][38] = "║"
Tablero[14][4] = "═"
Tablero[14][5] = "═"
Tablero[14][6] = "═"
Tablero[14][7] = "═"
Tablero[14][8] = "═"
Tablero[14][9] = "═"
Tablero[14][10] = "═"
Tablero[14][11] = "═"
Tablero[14][18] = "═"
Tablero[14][19] = "═"
Tablero[14][20] = "═"
Tablero[14][21] = "═"
Tablero[14][22] = "═"
Tablero[14][23] = "═"
Tablero[14][24] = "═"
Tablero[14][25] = "═"
Tablero[14][26] = "═"
Tablero[14][32] = "═"
Tablero[14][33] = "═"
Tablero[14][34] = "═"
Tablero[14][35] = "═"
Tablero[14][36] = "═"
Tablero[14][37] = "═"
Tablero[14][38] = "═"

jugador = "C"
seguir = False
desicion = '0'
while desicion != '2':
    puntaje = 0
    movimientos = 0
    name = ""
    seguir = False
    menu = """======= MENU =======
    1. Iniciar juego
    2. Salir"""
    print(menu)
    print("Seleccione una opción")
    desicion = input()
    if desicion == '1':
        print("Se iniciará una nueva partida")
        print("Ingrese su nick")
        nick = input()
        print(""""Controles:
        A=Derecha  S=Abajo  D=Derecha  W=Arriba  
        M=Fin del juego""")
        for i in range(x):
            for j in range(y):
                if Tablero[i][j] == "■":
                    Tablero[i][j] = " "

        for i in range(x):
            for j in range(y):
                if Tablero[i][j] == "C":
                    Tablero[i][j] = " "

        fr = 0
        while fr < 5:
            i = random.randrange(17)
            j = random.randrange(42)
            if Tablero[i][j] == " ":
                Tablero[i][j] = "■"
                fr += 1

        Tablero[9][22] = jugador
        posy = 9
        posx = 22

        while seguir != True:
            for f in range(x):
                for c in range(y):
                    print(Tablero[f][c],end=" ")
                print()

            print("puntaje ",puntaje)
            print("Movimientos ",movimientos)
            print("Seleccione su movimiento")
            move = input()
            if move == "A" or move == "a":
                Tablero[posy][posx] = " "
                posx = posx - 1
                movimientos += 1
                if posx == 0:
                    posx = 40
                if Tablero[posy][posx] == "═" or Tablero[posy][posx] == "║":
                    posx = posx + 1
                    movimientos = movimientos - 1
                if Tablero[posy][posx] == "■":
                    puntaje += random.randrange(1,5)
                    cr = False
                    while cr == False:
                        i = random.randrange(17)
                        j = random.randrange(42)
                        if Tablero[i][j] == " ":
                            cr = True
                            Tablero[i][j] = "■"
                Tablero[posy][posx] = jugador
                if puntaje >= 30:
                    seguir = True
                    print("Felicidades")
                    print("Puntaje: ",puntaje," movimientos: ",movimientos)

            elif move == "S" or move == "s":
                Tablero[posy][posx] = " "
                posy = posy + 1
                movimientos += 1
                if posy == 16:
                    posy = 1
                if Tablero[posy][posx] == "═" or Tablero[posy][posx] == "║":
                    posy = posy - 1
                    movimientos = movimientos - 1
                if Tablero[posy][posx] == "■":
                    puntaje += random.randrange(1,5)
                    cr = False
                    while cr == False:
                        i = random.randrange(17)
                        j = random.randrange(42)
                        if Tablero[i][j] == " ":
                            cr = True
                            Tablero[i][j] = "■"
                Tablero[posy][posx] = jugador
                if puntaje >= 30:
                    seguir = True
                    print("Felicidades")
                    print("Puntaje: ",puntaje," movimientos: ",movimientos)

            elif move == "D" or move == "d":
                Tablero[posy][posx] = " "
                posx = posx + 1
                movimientos += 1
                if posx == 41:
                    posx = 1
                if Tablero[posy][posx] == "═" or Tablero[posy][posx] == "║":
                    posx = posx - 1
                    movimientos = movimientos - 1
                if Tablero[posy][posx] == "■":
                    puntaje += random.randrange(1,5)
                    cr = False
                    while cr == False:
                        i = random.randrange(17)
                        j = random.randrange(42)
                        if Tablero[i][j] == " ":
                            cr = True
                            Tablero[i][j] = "■"
                Tablero[posy][posx] = jugador
                if puntaje >= 30:
                    seguir = True
                    print("Felicidades")
                    print("Puntaje: ",puntaje," movimientos: ",movimientos)

            elif move == "W" or move == "w":
                Tablero[posy][posx] = " "
                posy = posy - 1
                movimientos += 1
                if posy == 0:
                    posy = 15
                if Tablero[posy][posx] == "═" or Tablero[posy][posx] == "║":
                    posy = posy + 1
                    movimientos = movimientos - 1
                if Tablero[posy][posx] == "■":
                    puntaje += random.randrange(1,5)
                    cr = False
                    while cr == False:
                        i = random.randrange(17)
                        j = random.randrange(42)
                        if Tablero[i][j] == " ":
                            cr = True
                            Tablero[i][j] = "■"
                Tablero[posy][posx] = jugador
                if puntaje >= 30:
                    seguir = True
                    print("Felicidades")
                    print("Puntaje: ",puntaje," movimientos: ",movimientos)

            elif move == "M" or move == "m":
                Tablero[posy][posx] = " "
                seguir = True
                print("Puntaje: ",puntaje," movimientos: ",movimientos)

            else:
                print("Ingrese un valor válido")

    elif desicion == '2':
        quit()

    else:
        print("Error")



