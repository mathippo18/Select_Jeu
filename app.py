import os
import re
import platform
import sqlite3
import hashlib
import time
import filecmp
# Function to display login window
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Determine the operating system
system_exploit = platform.system()

is_logged_in = False # Variable to track login status
###Code###
# Function to install required packages based on the operating system
def config():
    if system_exploit == "Windows":
            os.system("pip install -r ../Conf/requirements.txt")
    elif system_exploit == "Linux":
            os.system("pip install -r ../Conf/requirements_linux.txt")

def show_login_window():
    
    global is_logged_in
    if is_logged_in:
        messagebox.showinfo("Information", "Vous êtes déjà connecté.")
        return

    login_window = tk.Toplevel()
    login_window.title("Login")
    login_window.resizable(False, False)


    action_label = tk.Label(login_window, text="Sélectionnez une action:")
    action_label.pack(pady=10)

    action_var = tk.StringVar(value="Connecter")  # Variable to store the selected action
    action_combobox = ttk.Combobox(login_window, textvariable=action_var, values=["Connecter", "S'inscrire"])
    action_combobox.pack(pady=5)

    id_label = tk.Label(login_window, text="Identifiant:")
    id_label.pack(pady=5)

    id_entry = tk.Entry(login_window)
    id_entry.pack(pady=5)

    password_label = tk.Label(login_window, text="Mot de passe:")
    password_label.pack(pady=5)

    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    def handle_login():
        global is_logged_in
        action = action_var.get()
        if action == "Connecter":
            global id
            id = id_entry.get()
            password = password_entry.get()
            hash_object = hashlib.sha3_512(password.encode())
            hex_digest = hash_object.hexdigest()
            # Connect to the database
            sqliteConnection = sqlite3.connect('../DataBase/connect.db')
            cursor = sqliteConnection.cursor()
            # Check if the provided credentials exist in the database
            query = '''Select * From Id WHERE Pseudo=? AND Password=?;'''
            cursor.execute(query,(id, hex_digest))
            output = cursor.fetchall()
            while len(output) == 0 :  # Loop until valid credentials are provided
                messagebox.showerror("Error", "Pseudo ou Mot de passe incorrect")
                return
            messagebox.showinfo("Success", "Bienvenue " + id)
            login_window.destroy()
            sqliteConnection.commit()
            cursor.close()
            sqliteConnection.close()
            is_logged_in = True  # Set login status to True after successful login
        elif action == "S'inscrire":
            id = id_entry.get()
            password = password_entry.get()
            hash_object = hashlib.sha3_512(password.encode())
            hex_digest = hash_object.hexdigest()
            # Connect to the database
            sqliteConnection = sqlite3.connect('../DataBase/connect.db')
            cursor = sqliteConnection.cursor()
            # Check if the provided username already exists
            query = '''Select * From Id WHERE Pseudo=? ;'''
            cursor.execute(query,(id,))
            output = cursor.fetchall()
            if len(output) == 0:  # Username is available
                # Insert new user into the database
                query = '''Insert Into Id Values (?, ?);'''
                cursor.execute(query,(id, hex_digest))
                query = '''Insert Into HighScore Values (?, 0, 0, 0, 0);'''
                cursor.execute(query,(id, ))
                messagebox.showinfo("Success", "Bienvenue " + id)
                login_window.destroy()
            else:
                # Prompt user to choose a different username
                messagebox.showerror("Error", "Nom utilisateur, veuillez en prendre un autre !")
                id_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                return
            sqliteConnection.commit()
            cursor.close()
            sqliteConnection.close() 

    login_button = tk.Button(login_window, text="Valider", command=handle_login)
    login_button.pack(pady=5)


# Function to display game selection menu
def selection():
    selection_window = tk.Toplevel()
    selection_window.title("Game Selection")
    selection_window.resizable(False, False)

    games_label = tk.Label(selection_window, text="Bienvenue sur la séléction de jeu de Mathéo\nVous avez le choix entre 9 jeux :")
    games_label.pack(pady=10)

    games = ["Une roulette de casino", "Othello", "Space invaders", "Morpion", "Snake Eater", "Un pendu", "Casse brique", "Tetris", "sudoku"]
    for i, game in enumerate(games, start=1):
        game_button = tk.Button(selection_window, text=game, command=lambda game=game: launch_game(game))
        game_button.pack(pady=5)

    # Additional options
    additional_options_label = tk.Label(selection_window, text="Options supplémentaires:")
    additional_options_label.pack(pady=20)

    options = ["Visiter mon github", "Voir vos meilleurs scores", "Modifier le mot de passe", "Supprimer un compte"]
    for i, option in enumerate(options, start=len(games)+1):
        option_button = tk.Button(selection_window, text=option, command=lambda option=option: handle_additional_option(option))
        option_button.pack(pady=5)

# Function to handle additional options
def handle_additional_option(option):
    if option == "Visiter mon github":
        url = "https://github.com/mathippo18"
        os.system(f"start {url}")
    elif option == "Voir vos meilleurs scores":
        show_high_scores()
    elif option == "Modifier le mot de passe":
        change_password()
    elif option == "Supprimer un compte":
        delete_account()

# Function to show high scores
def show_high_scores():
    sqliteConnection = sqlite3.connect('../DataBase/connect.db')
    cursor = sqliteConnection.cursor()
    query = '''Select Identifiant From HighScore ;'''
    cursor.execute(query)
    output = cursor.fetchall()
    highscores_window = tk.Toplevel()
    highscores_window.title("Meilleurs Scores")
    highscores_window.resizable(False, False)

    id_label = tk.Label(highscores_window, text="Identifiant:")
    id_label.pack(pady=5)
    tableau = []
    for row in output:
        tableau.append(row[0])
    id_entry = ttk.Combobox(highscores_window, values=tableau)
    id_entry.pack(pady=5)

    highscores_text = tk.Text(highscores_window, height=10, width=30)
    highscores_text.pack(pady=5)
    sqliteConnection.commit()
    cursor.close()
    sqliteConnection.close() 
    def show_highscores():
        id_value = id_entry.get()

        # Vérification des champs vides
        if not id_value:
            tk.messagebox.showerror("Erreur", "Veuillez entrer un identifiant.")
            return

        try:
            # Connexion à la base de données
            sqliteConnection = sqlite3.connect('../DataBase/connect.db')
            cursor = sqliteConnection.cursor()

            # Récupération des meilleurs scores du joueur
            query = '''SELECT * FROM HighScore WHERE Identifiant=?;'''
            cursor.execute(query, (id_value,))
            scores = cursor.fetchall()

            # Affichage des meilleurs scores dans la zone de texte
            highscores_text.delete('1.0', tk.END)
            if len(scores) > 0:
                for row in scores:
                    highscores_text.insert(tk.END, "Joueur: {}\n".format(row[0]))
                    highscores_text.insert(tk.END, "Space invaders: {}\n".format(row[1]))
                    highscores_text.insert(tk.END, "Snake : {}\n".format(row[2]))
                    highscores_text.insert(tk.END, "Roulette : {}\n".format(row[3]))
                    highscores_text.insert(tk.END, "Tétris : {}\n".format(row[4]))
            else:
                highscores_text.insert(tk.END, "Aucun score trouvé pour cet identifiant.")

            sqliteConnection.commit()

        except Exception as e:
            tk.messagebox.showerror("Erreur", str(e))

        finally:
            # Fermeture de la connexion à la base de données
            if sqliteConnection:
                cursor.close()
                sqliteConnection.close()

    show_button = tk.Button(highscores_window, text="Afficher les Meilleurs Scores", command=show_highscores)
    show_button.pack(pady=5)

# Function to change password
def change_password():
    change_password_window = tk.Toplevel()
    change_password_window.title("Modifier le Mot de Passe")
    change_password_window.resizable(False, False)

    id_label = tk.Label(change_password_window, text="Identifiant:")
    id_label.pack(pady=5)

    id_entry = tk.Entry(change_password_window)
    id_entry.pack(pady=5)

    current_password_label = tk.Label(change_password_window, text="Mot de passe actuel:")
    current_password_label.pack(pady=5)

    current_password_entry = tk.Entry(change_password_window, show="*")
    current_password_entry.pack(pady=5)

    new_password_label = tk.Label(change_password_window, text="Nouveau mot de passe:")
    new_password_label.pack(pady=5)

    new_password_entry = tk.Entry(change_password_window, show="*")
    new_password_entry.pack(pady=5)

    confirm_password_label = tk.Label(change_password_window, text="Confirmez le nouveau mot de passe:")
    confirm_password_label.pack(pady=5)

    confirm_password_entry = tk.Entry(change_password_window, show="*")
    confirm_password_entry.pack(pady=5)

    def change_password():
        id_value = id_entry.get()
        current_password_value = current_password_entry.get()
        new_password_value = new_password_entry.get()
        confirm_password_value = confirm_password_entry.get()

        # Vérification des champs vides
        if not id_value or not current_password_value or not new_password_value or not confirm_password_value:
            tk.messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            change_password_window.destroy()
            return

        # Vérification de la correspondance des nouveaux mots de passe
        if new_password_value != confirm_password_value:
            tk.messagebox.showerror("Erreur", "Les nouveaux mots de passe ne correspondent pas.")
            return

        try:
            # Connexion à la base de données
            sqliteConnection = sqlite3.connect('../DataBase/connect.db')
            cursor = sqliteConnection.cursor()

            # Vérification du mot de passe actuel
            hash_object = hashlib.sha3_512(current_password_value.encode())
            hex_digest = hash_object.hexdigest()
            query = '''SELECT * FROM Id WHERE Pseudo=? AND Password=?;'''
            cursor.execute(query, (id_value, hex_digest))
            output = cursor.fetchall()

            if len(output) == 0:
                tk.messagebox.showerror("Erreur", "Mot de passe actuel incorrect.")
                return

            # Hashage du nouveau mot de passe et mise à jour dans la base de données
            new_hash_object = hashlib.sha3_512(new_password_value.encode())
            new_hex_digest = new_hash_object.hexdigest()
            update_query = '''UPDATE Id SET Password=? WHERE Pseudo=? AND Password=?;'''
            cursor.execute(update_query, (new_hex_digest, id_value, hex_digest))
            sqliteConnection.commit()

            tk.messagebox.showinfo("Succès", "Le mot de passe a été modifié avec succès.")


        except Exception as e:
            tk.messagebox.showerror("Erreur", str(e))

        finally:
            # Fermeture de la connexion à la base de données
            if sqliteConnection:
                cursor.close()
                sqliteConnection.close()

    change_button = tk.Button(change_password_window, text="Modifier le Mot de Passe", command=change_password)
    change_button.pack(pady=5)

# Function to delete account
def delete_account():
    delete_account_window = tk.Toplevel()
    delete_account_window.title("Supprimer le Compte")
    delete_account_window.resizable(False, False)

    id_label = tk.Label(delete_account_window, text="Identifiant:")
    id_label.pack(pady=5)

    id_entry = tk.Entry(delete_account_window)
    id_entry.pack(pady=5)

    password_label = tk.Label(delete_account_window, text="Mot de passe:")
    password_label.pack(pady=5)

    password_entry = tk.Entry(delete_account_window, show="*")
    password_entry.pack(pady=5)

    def delete_account():
        id_value = id_entry.get()
        password_value = password_entry.get()

        # Vérification des champs vides
        if not id_value or not password_value:
            tk.messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        try:
            # Connexion à la base de données
            sqliteConnection = sqlite3.connect('../DataBase/connect.db')
            cursor = sqliteConnection.cursor()

            # Vérification du mot de passe
            hash_object = hashlib.sha3_512(password_value.encode())
            hex_digest = hash_object.hexdigest()
            query = '''SELECT * FROM Id WHERE Pseudo=? AND Password=?;'''
            cursor.execute(query, (id_value, hex_digest))
            output = cursor.fetchall()

            if len(output) == 0:
                tk.messagebox.showerror("Erreur", "Identifiant ou Mot de passe incorrect.")
                return

            # Suppression du compte de la base de données
            delete_query = '''DELETE FROM Id WHERE Pseudo=?;'''
            delete_highscore_query = '''DELETE FROM HighScore WHERE Identifiant=?;'''
            cursor.execute(delete_query, (id_value,))
            cursor.execute(delete_highscore_query, (id_value,))
            sqliteConnection.commit()

            tk.messagebox.showinfo("Succès", "Le compte a été supprimé avec succès.")
            delete_account_window.destroy()  # Fermer la fenêtre après suppression du compte

        except Exception as e:
            tk.messagebox.showerror("Erreur", str(e))

        finally:
            # Fermeture de la connexion à la base de données
            if sqliteConnection:
                cursor.close()
                sqliteConnection.close()

    delete_button = tk.Button(delete_account_window, text="Supprimer le Compte", command=delete_account)
    delete_button.pack(pady=5)

# Function to launch selected game
def launch_game(game):
    if game == "Une roulette de casino":
        cmd = "python3 ../Jeux/ZCasino/ZCasino.py "+ id
        os.system(cmd)
    elif game == "Othello":
        cmd = "python3 ../Jeux/reversi/reversi.py"
        os.system(cmd)
    elif game == "Space invaders":
        cmd = "python3 ../Jeux/Space_Invaders/Code/Main.py "+ id
        os.system(cmd)
    elif game == "Morpion":
        cmd = "python3 ../Jeux/Morpion/morpion.py"
        os.system(cmd)
    elif game == "Snake Eater":
        cmd = "python3 ../Jeux/Snake/snake.py "+ id
        os.system(cmd)
    elif game == "Un pendu":
        cmd = "python3 ../Jeux/Hangman/hangman.py"
        os.system(cmd)
    elif game == "Casse brique":
        if system_exploit == "Windows":
            cmd = "cd ../Jeux/Casse_brique/ && casse_brique.html && cd ../.."
            os.system(cmd)
        elif system_exploit == "Linux":
            cmd = "x-www-browser ../Jeux/Casse_brique/casse_brique.html"
            os.system(cmd)
        else:
            print("Ce programme n'a pas été testé sur MacOS, il sera donc pas lancé")
    elif game == "Tetris":
        cmd = "python3 ../Jeux/python-tetris/tetris.py "+ id
        os.system(cmd)
    elif game == "sudoku":
        cmd = "python3 ../Jeux/Sudoku/GUI.py"
        os.system(cmd)

# Initialize Tkinter
try:
    root = tk.Tk()
    root.title("Game Launcher")

    # Create buttons for login and game selection
    login_button = tk.Button(root, text="Login", command=show_login_window)
    login_button.pack(pady=20)

    selection_button = tk.Button(root, text="Game Selection", command=selection)
    selection_button.pack(pady=20)

    root.mainloop()
except ModuleNotFoundError:
    config()
    root = tk.Tk()
    root.title("Game Launcher")

    # Create buttons for login and game selection
    login_button = tk.Button(root, text="Login", command=show_login_window)
    login_button.pack(pady=20)

    selection_button = tk.Button(root, text="Game Selection", command=selection)
    selection_button.pack(pady=20)

    root.mainloop()