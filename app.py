import os
import re
import platform
import sqlite3
import hashlib
import time
import filecmp

os.system("pip freeze > config.txt")
comparaison = filecmp.cmp("config.txt","requirements.txt")
if comparaison == False:
    os.system("pip install -r requirements.txt")


###Database###

connect = input("Tapez 1 pour vous connecter \nTapez 2 pour vous inscrire\n")
intconnect = int(connect)
while intconnect >= 3:
    connect = input("Tapez 1 pour vous connecter \nTapez 2 pour vous inscrire\n")
    intconnect = int(connect)
if connect == '1':
    id = input("Quel est votre identifiant ? \n")
    password = input("Quel est votre mot de passe ? \n")
    hash_object = hashlib.sha3_512(password.encode())
    hex_digest = hash_object.hexdigest()
    sqliteConnection = sqlite3.connect('DataBase/connect.db')
    cursor = sqliteConnection.cursor()
    query = '''Select * From Id WHERE Pseudo=? AND Password=?;'''
    cursor.execute(query,(id, hex_digest))
    output = cursor.fetchall()
    while len(output) == 0 : 
        print("Pseudo ou Mot de passe incorrect")
        id = input("Quel est votre identifiant ? \n")
        password = input("Quel est votre mot de passe ? \n")
        hash_object = hashlib.sha3_512(password.encode())
        hex_digest = hash_object.hexdigest()
        query = '''Select * From Id WHERE Pseudo=? AND Password = ?;'''
        cursor.execute(query,(id, hex_digest))
        output = cursor.fetchall()
    print("Bienvenue ",id)
    sqliteConnection.commit()
    cursor.close()
    sqliteConnection.close()      
elif connect == "2":
    id = input("Quel est votre identifiant ? \n")
    password = input("Quel est votre mot de passe ? \n")
    hash_object = hashlib.sha3_512(password.encode())
    hex_digest = hash_object.hexdigest()
    sqliteConnection = sqlite3.connect('DataBase/connect.db')
    cursor = sqliteConnection.cursor()
    query = '''Select * From Id WHERE Pseudo=? ;'''
    cursor.execute(query,(id,))
    output = cursor.fetchall()
    if len(output) == 0:
        query = '''Insert Into Id Values (?, ?);'''
        cursor.execute(query,(id, hex_digest))
        query = '''Insert Into HighScore Values (?, 0, 0, 0, 0);'''
        cursor.execute(query,(id, ))
        print("Bienvenue ",id)
        sqliteConnection.commit()
        cursor.close()
        sqliteConnection.close()
    else:
        print("Nom utilisateur, veuillez en prendre un autre !")
        id = input("Quel est votre identifiant ? \n")
        password = input("Quel est votre mot de passe ? \n")
        hash_object = hashlib.sha3_512(password.encode())
        hex_digest = hash_object.hexdigest()
        sqliteConnection = sqlite3.connect('DataBase/connect.db')
        cursor = sqliteConnection.cursor()
        query = '''Select * From Id WHERE Pseudo=? ;'''
        cursor.execute(query,(id,))
        output = cursor.fetchall()
        if len(output) == 0:
            query = '''Insert Into Id Values (?, ?);'''
            cursor.execute(query,(id, hex_digest))
            query = '''Insert Into HighScore Values (?, 0, 0, 0, 0);'''
            cursor.execute(query,(id, ))
            print("Bienvenue ",id)
            sqliteConnection.commit()
            cursor.close()
            sqliteConnection.close() 


###Code###
system_exploit = platform.system()
format = "[0-9]*"
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
    print(" - 11 Voir vos meilleurs scores ")
    print(" - 12 Modifier le mot de passe ")
    print(" - 13 Supprimer un compte ")
    jeu_souhaité = input("Vous voulez jouer a quel jeu ? : ")
    test = re.search(format, jeu_souhaité)
    while test == None:
        print("Veuillez renseigner le numéro lié au jeu/fonction")
        jeu_souhaité = input("Vous voulez jouer a quel jeu ? : ")
        test = re.search(format, jeu_souhaité)
    jeu = int(jeu_souhaité)
    if jeu == 1:
        cmd = "python3 Jeux/ZCasino/ZCasino.py "+ id
        os.system(cmd)
    if jeu == 2:
        cmd = "python3 Jeux/reversi/reversi.py"
        os.system(cmd)
    if jeu == 3:
        cmd = "python3 Jeux/Space_Invaders/Code/Main.py "+ id
        os.system(cmd)
    if jeu == 4:
        cmd = "python3 Jeux/Morpion/morpion.py"
        os.system(cmd) 
    if jeu == 5:
        cmd = "python3 Jeux/Snake/snake.py "+ id
        os.system(cmd)
    if jeu == 6:
        cmd = "python3 Jeux/Hangman/hangman.py"
        os.system(cmd)
    if jeu == 7:
        if system_exploit == "Windows":
            cmd = "cd Jeux/Casse_brique/ && casse_brique.html && cd ../.."
            os.system(cmd)
        elif system_exploit == "Linux":
            cmd = "x-www-browser Jeux/Casse_brique/casse_brique.html"
            os.system(cmd)
        else:
            print("Ce programme n'a pas été testé sur MacOS, il sera donc pas lancé")
    if jeu == 8:
        cmd = "python3 Jeux/python-tetris/tetris.py "+ id
        os.system(cmd)
    if jeu == 9:
        cmd = "python3 Jeux/Sudoku/GUI.py"
        os.system(cmd)
    if jeu == 10:
        if system_exploit == "Windows":
            cmd = "start microsoftedge.exe https://github.com/mathippo18"
            os.system(cmd)
        elif system_exploit == "Linux":
            cmd = "x-www-browser https://github.com/mathippo18"
            os.system(cmd)
        else:
            print("Ce programme n'a pas été testé sur MacOS, il sera donc pas lancé")
    if jeu == 11:
        sqliteConnection = sqlite3.connect('DataBase/connect.db')
        cursor = sqliteConnection.cursor()
        query = '''Select * From HighScore WHERE Identifiant=? ; '''
        cursor.execute(query,(id,))
        score = cursor.fetchall()
        for row in score:
            print("Pseudo: ", row[0])
            print("Space Invaders: ", row[1])
            print("Snake: ", row[2])
            print("Roulette: ", row[3])
            print("Tetris: ", row[4])
        time.sleep(6)
        sqliteConnection.commit()
        cursor.close()
        sqliteConnection.close()
    if jeu == 12:
        sqliteConnection = sqlite3.connect('DataBase/connect.db')
        cursor = sqliteConnection.cursor()
        password = input("Quel est votre mot de passe actuel ? \n")
        hash_object = hashlib.sha3_512(password.encode())
        hex_digest = hash_object.hexdigest()
        query = '''Select * From Id WHERE Pseudo=? AND Password=?;'''
        cursor.execute(query,(id, hex_digest))
        output = cursor.fetchall()
        if len(output) == 0 : 
            print("Mot de passe incorrect")
            sqliteConnection.commit()
            cursor.close()
            sqliteConnection.close()
        else:
            new_password = input("Quel est votre nouveau mot de passe ? \n")
            new_password_confirm = input("Confirmez votre nouveau mot de passe ? \n")
            while new_password != new_password_confirm:
                new_password = input("Quel est votre nouveau mot de passe ? \n")
                new_password_confirm = input("Confirmez votre nouveau mot de passe ? \n")
            new_hash_object = hashlib.sha3_512(new_password.encode())
            new_hex_digest = new_hash_object.hexdigest()
            query = '''UPDATE Id SET Password = ? WHERE Pseudo=? AND Password = ?; '''
            cursor.execute(query,(new_hex_digest,id, hex_digest))
            sqliteConnection.commit()
            cursor.close()
            sqliteConnection.close()
    if jeu == 13:
        sqliteConnection = sqlite3.connect('DataBase/connect.db')
        cursor = sqliteConnection.cursor()
        password = input("Quel est votre mot de passe ? \n")
        hash_object = hashlib.sha3_512(password.encode())
        hex_digest = hash_object.hexdigest()
        query = '''Select * From Id WHERE Pseudo=? AND Password=?;'''
        cursor.execute(query,(id, hex_digest))
        output = cursor.fetchall()
        if len(output) == 0 : 
            print("Mot de passe incorrect")
            sqliteConnection.commit()
            cursor.close()
            sqliteConnection.close()
        else:
            query = '''Delete From Id WHERE Pseudo=? ; '''
            query2 =''' Delete From HighScore WHERE Identifiant=? ;'''
            cursor.execute(query,(id,))
            sqliteConnection.commit()
            cursor.execute(query2,(id,))
            sqliteConnection.commit()
            cursor.close()
            sqliteConnection.close()
            print("Au revoir et bonne continuation")
            quit()
            


jeu = None



try:
    while jeu is None or jeu >= 13:
        selection()
except KeyboardInterrupt:
    print("\nBonne journée et a la prochaine !")
 


