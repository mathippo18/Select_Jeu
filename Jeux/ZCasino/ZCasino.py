import tkinter as tk
from tkinter import messagebox
import random

class RouletteGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de Roulette")
        self.solde = 1000

        self.label_solde = tk.Label(master, text="Solde: ${}".format(self.solde))
        self.label_solde.pack()

        self.label_mise = tk.Label(master, text="Mise:")
        self.label_mise.pack()
        self.mise_entry = tk.Entry(master)
        self.mise_entry.pack()

        self.label_numero = tk.Label(master, text="Numéro misé (entre 0 et 50) ou couleur (rouge/noir):")
        self.label_numero.pack()
        self.numero_entry = tk.Entry(master)
        self.numero_entry.pack()

        self.spin_button = tk.Button(master, text="Tourner la roulette", command=self.tourner_roulette)
        self.spin_button.pack()

    def tourner_roulette(self):
        try:
            mise = int(self.mise_entry.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer une mise valide.")
            return

        if mise <= 0:
            messagebox.showerror("Erreur", "La mise doit être supérieure à zéro.")
            return

        numero_mise = self.numero_entry.get().lower()

        if numero_mise.isdigit():
            numero_mise = int(numero_mise)
            if not 0 <= numero_mise <= 50:
                messagebox.showerror("Erreur", "Le numéro misé doit être entre 0 et 50.")
                return
            couleur_gagnante = "N/A"
        elif numero_mise in ["rouge", "noir"]:
            couleur_gagnante = random.choice(["rouge", "noir"])
            numero_mise = None
        else:
            messagebox.showerror("Erreur", "Le numéro ou la couleur misé doit être un nombre entre 0 et 50 ou 'rouge'/'noir'.")
            return

        numero_gagnant = random.randint(0, 50)
        couleur_gagnante_numero = self.get_numero_couleur(numero_gagnant)
        messagebox.showinfo("Résultat", "Le numéro gagnant est le {} ({})".format(numero_gagnant, couleur_gagnante_numero))

        if (numero_mise is not None and numero_mise == numero_gagnant) or (numero_mise is None and couleur_gagnante == couleur_gagnante_numero):
            if numero_mise is not None:
                gain = mise * 35
            else:
                gain = mise * 2
            messagebox.showinfo("Résultat", "Félicitations ! Vous avez gagné ${}".format(gain))
        else:
            messagebox.showinfo("Résultat", "Désolé, vous avez perdu.")
            gain = -mise

        self.solde += gain
        if self.solde < 0:
            self.solde = 0
        self.label_solde.config(text="Solde: ${}".format(self.solde))

    def get_numero_couleur(self, numero):
        if numero == 0:
            return "vert"
        elif (numero >= 1 and numero <= 10) or (numero >= 19 and numero <= 28):
            return "rouge" if numero % 2 == 1 else "noir"
        else:
            return "noir" if numero % 2 == 1 else "rouge"

def main():
    root = tk.Tk()
    roulette_game = RouletteGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
