import tkinter as tk
from tkinter import messagebox
import numpy as np

class MorpionGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Morpion")

        self.grille = np.zeros((3, 3))
        self.jIa = 1
        self.jHumain = 2
        self.currentplayer = self.jHumain  # L'humain commence
        self.mode = tk.IntVar(value=1)  # 1 pour jouer contre l'IA, 2 pour jouer contre un autre joueur

        # Création des boutons radio pour sélectionner le mode de jeu
        tk.Radiobutton(master, text="Joueur vs IA", variable=self.mode, value=1).grid(row=0, column=0)
        tk.Radiobutton(master, text="Joueur vs Joueur", variable=self.mode, value=2).grid(row=0, column=1)

        self.button_grid = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(master, text="", width=10, height=5, command=lambda i=i, j=j: self.jouer_coup(i, j))
                button.grid(row=i+1, column=j)
                row_buttons.append(button)
            self.button_grid.append(row_buttons)

    def AfficherGrille(self):
        for i in range(3):
            for j in range(3):
                if self.grille[i][j] == self.jIa:
                    self.button_grid[i][j].config(text="❌")
                elif self.grille[i][j] == self.jHumain:
                    self.button_grid[i][j].config(text="⭕")
                else:
                    self.button_grid[i][j].config(text="")

    def jouer_coup(self, i, j):
        if self.grille[i][j] == 0:
            self.grille[i][j] = self.currentplayer
            self.AfficherGrille()
            self.check_victoire()
            if self.mode.get() == 1:
                self.currentplayer = self.jIa if self.currentplayer == self.jHumain else self.jHumain
                self.jouer_IA()
            else:
                self.currentplayer = self.jIa if self.currentplayer == self.jHumain else self.jHumain

    def check_victoire(self):
        for i in range(3):
            if self.grille[i][0] == self.grille[i][1] == self.grille[i][2] != 0:
                self.afficher_message_victoire(self.grille[i][0])
                return
            if self.grille[0][i] == self.grille[1][i] == self.grille[2][i] != 0:
                self.afficher_message_victoire(self.grille[0][i])
                return
        if self.grille[0][0] == self.grille[1][1] == self.grille[2][2] != 0:
            self.afficher_message_victoire(self.grille[0][0])
            return
        if self.grille[0][2] == self.grille[1][1] == self.grille[2][0] != 0:
            self.afficher_message_victoire(self.grille[0][2])
            return
        if np.all(self.grille != 0):
            self.afficher_message_victoire(None)

    def afficher_message_victoire(self, gagnant):
        if gagnant == self.jIa:
            messagebox.showinfo("Fin de partie", "X gagne !")
        elif gagnant == self.jHumain:
            messagebox.showinfo("Fin de partie", "O gagne!")
        else:
            messagebox.showinfo("Fin de partie", "Match nul !")
        self.master.destroy()  # Fermer la fenêtre à la fin de la partie

    def jouer_IA(self):
        if np.any(self.grille == 0):
            i, j = self.minimax_decision()
            self.grille[i][j] = self.jIa
            self.AfficherGrille()
            self.check_victoire()
            self.currentplayer = self.jHumain

    def minimax_decision(self):
        meilleur_score = -np.inf
        meilleur_coup = None
        for i in range(3):
            for j in range(3):
                if self.grille[i][j] == 0:
                    self.grille[i][j] = self.jIa
                    score = self.minimax_value(False)
                    self.grille[i][j] = 0
                    if score > meilleur_score:
                        meilleur_score = score
                        meilleur_coup = (i, j)
        return meilleur_coup

    def minimax_value(self, is_maximizing):
        if np.any(self.grille == 0):
            gagnant = self.terminal_test()
            if gagnant != 0:
                return 1 if gagnant == self.jIa else -1
            if is_maximizing:
                value = -np.inf
                for i in range(3):
                    for j in range(3):
                        if self.grille[i][j] == 0:
                            self.grille[i][j] = self.jIa
                            value = max(value, self.minimax_value(False))
                            self.grille[i][j] = 0
                return value
            else:
                value = np.inf
                for i in range(3):
                    for j in range(3):
                        if self.grille[i][j] == 0:
                            self.grille[i][j] = self.jHumain
                            value = min(value, self.minimax_value(True))
                            self.grille[i][j] = 0
                return value
        else:
            return 0

    def terminal_test(self):
        for i in range(3):
            if self.grille[i][0] == self.grille[i][1] == self.grille[i][2] != 0:
                return self.grille[i][0]
            if self.grille[0][i] == self.grille[1][i] == self.grille[2][i] != 0:
                return self.grille[0][i]
        if self.grille[0][0] == self.grille[1][1] == self.grille[2][2] != 0:
            return self.grille[0][0]
        if self.grille[0][2] == self.grille[1][1] == self.grille[2][0] != 0:
            return self.grille[0][2]
        if np.all(self.grille != 0):
            return 0
        return None

def main():
    root = tk.Tk()
    morpion_game = MorpionGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
