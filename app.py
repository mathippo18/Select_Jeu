import os
import re
###Code###
format = "[0-9]"
def selection():
    print("Bonjour sur la séléction de jeu de Mathéo")
    print("Vous avez le choix entre 9 jeux :")
    print(" - 1 Une roulette de casino ")
    print(" - 2 Othello ")
    print(" - 3 Space invaders ")
    print(" - 4 Morpion ")
    print(" - 5 Snake Eater")
    print(" - 6 Un pendu ")
    print(" - 7 Casse brique ")
    print(" - 8 Tetris ")
    print(" - 9 sudoku")
    print(" - 10 visiter mon github ")
    jeu_souhaité = input("Vous voulez jouer a quel jeu ? : ")
    test = re.search(format, jeu_souhaité)
    if test:
        jeu = int(jeu_souhaité)
        if jeu == 1:
            cmd = "python3 Jeux/ZCasino/ZCasino.py"
            os.system(cmd)
        if jeu == 2:
            cmd = "python3 Jeux/reversi/reversi.py"
            os.system(cmd)
        if jeu == 3:
            cmd = "python3 Jeux/Space_Invaders/Code/Main.py"
            os.system(cmd)
        if jeu == 4:
            cmd = "python3 Jeux/Morpion/morpion.py"
            os.system(cmd) 
        if jeu == 5:
            cmd = "python3 Jeux/Snake/snake.py"
            os.system(cmd)
        if jeu == 6:
            cmd = "python3 Jeux/Hangman/hangman.py"
            os.system(cmd)
        if jeu == 7:
            cmd = "cd Jeux/Casse_brique/ && casse_brique.html && cd ../.."
            os.system(cmd)
        if jeu == 8:
            cmd = "python3 Jeux/python-tetris/tetris.py"
            os.system(cmd)
        if jeu == 9:
            cmd = "python3 Jeux/Sudoku/GUI.py"
            os.system(cmd)
        if jeu == 10:
            cmd = "start microsoftedge.exe https://github.com/mathippo18"
            os.system(cmd)


jeu = None

try:
    while jeu is None or jeu >= 11:
        selection()
except KeyboardInterrupt:
    print("\nBonne journée et a la prochaine !")


 


