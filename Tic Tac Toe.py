# _*_ coding: utf-8 _*_

from random import randint

field = ["run",
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]
game_run = True

def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])

def usr_input():
    while True:
        # Überprüfen ob Spiel fertig
        if field[0] == "run":
            play_move = input("Bitte Feld Eingeben oder exit für Beenden: ")
            #Überprüfung ob zahl
            try:
                play_move = int(play_move)
            except ValueError:
                    print("Bitte eine Zahl von 1 bis 9 eingeben")
            else:
                #Überprüfung ob zahl zwischen 1 und 9 ist
                if play_move >= 1 and play_move <= 9:
                    #Überprüfung ob Feld Besetzt
                    if field_free(play_move):
                        return play_move
                    else:
                        print("Feld ist Leider Schon Besetzt!")
                else:
                    print("Zahl muss zwischen 1 und 9 liegen")
        else:
            play_move = input("Nochmal mit ja oder exit ")
            play_move = play_move.lower()
            return play_move

def set_move(move,player):
    move = move
    player = player
    if player == "X":
        field[move] = "X"
    else:
        field[move] = "O"

def ki_player():
    move = randint(1, 9)
    if field_free(move):
        set_move(move, "O")
    else:
        ki_player()

def field_free(move):
    #gibt True zurück wen Feld Frei
    if field[move] == "X" or field[move] == "O":
        return False
    else:
        return True

def win():
    #kontrolle Reihen
    for i in range(1, 8, 3):
        if field[i] == field[i + 1] == field[i + 2]:
            if field[i] == "X":
                field[0] = "won"
                break
            else:
                field[0] = "loose"
                break
    #kontrolle Spalten
    i = 1
    for i in range(1, 4):
        if field[i] == field[i + 3] == field[i + 6]:
            if field[i] == "X":
                field[0] = "won"
                break
            else:
                field[0] = "loose"
                break
    #kontrolle Diagonalen
    if field[1] == field[5] == field[9]:
        if field[1] == "X":
            field[0] = "won"
        else:
            field[0] = "loose"
    if field[3] == field[5] == field[7]:
        if field[3] == "X":
            field[0] = "won"
        else:
            field[0] = "loose"

def field_full():
    #kontrolle Feld voll
    for i in range(1, 10):
        if field[i] == "O" or field[i] == "X":
            if i == 9:
                field[0] = "full"
        else:
            break

def new_field():
    #feld neu erstellen
    for i in range(10):
        if i == 0:
            field[i] = "run"
        else:
            field[i] = str(i)

def re_run():
    print_field()
    while True:
        inp = usr_input()
        if inp.isdigit():
            print("Bitte ja oder exit eingeben ")
        #gibt True zurück wen exit eingegeben wird
        elif inp == "exit":
           return True
        elif inp == "ja":
            new_field()
            break
        else:
            print("Bitte ja oder exit eingeben ")

def run_game():
    while True:
        win()
        if field[0] == "won":
            print("Du hast Gewonnen!")
            if re_run():
                break
        if field[0] == "loose":
            print("Verloren!")
            if re_run():
                break
        if field[0] == "full":
            print("Unentschiden!")
            if re_run():
                break
        if field[0] == "run":
            print_field()
            inp = usr_input()
            if inp == "exit":
                break
            set_move(inp,"X")
            field_full()
            if field[0] == "run":
                ki_player()

run_game()
