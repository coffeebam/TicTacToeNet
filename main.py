spielfeld = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cap = 9

i = 0
for n in range(3):
    print("|", end = "")
    for j in range(3):
        print(spielfeld[i], end = "|")
        i = i + 1
    print()

def ende(spieler, feld):
    kombinationen = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(8):
        for n in range(3):
            if kombinationen[i][n] == feld:
                if spielfeld[kombinationen[i][0]] == spieler and spielfeld[kombinationen[i][1]] == spieler and spielfeld[kombinationen[i][2]] == spieler:
                    return True
    return False


def setzen(spieler):
    while True:
        position = input("Spieler " + spieler + ", an welche Position willst du setzen? (1-9)\n")
        position = int(position)
        if 1 <= position <= 9:
            if type(spielfeld[position - 1]) == int:
                break
    spielfeld[position - 1] = spieler

    global cap
    cap -= 1
    if ende(spieler, position - 1):
        print("Spieler " + spieler + " hat gewonnen!")
        drucken()
        quit()
    if cap == 0:
        print("Unentschieden!")
        drucken()
        quit()


def drucken():
    i = 0
    for n in range(3):
        print("|", end="")
        for j in range(3):
            if type(spielfeld[i]) == str:
                print(spielfeld[i], end="|")
            else:
                print(" ", end="|")
            i = i + 1
        print()

while True:
    setzen("X")
    drucken()
    setzen("O")
    drucken()