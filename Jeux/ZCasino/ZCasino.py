import os
import random
import math
import ZCasino_jeu
import ZCasino_joueur

try:
        # ****** programme du jeu de la roulette **********
        print("Bienvenue au ZCasino, voici le jeu de la Roulette !")

        # appel de variables 'nulles'
        pseudo = 0
        porte_monnaie = 0
        numero_mise = 0
        somme_misee = 0
        # description du joueur
        joueur1 = ZCasino_joueur.Joueur(pseudo, porte_monnaie, numero_mise, somme_misee)
        pseudo = joueur1.nom_joueur(pseudo)
        porte_monnaie = joueur1.argent_joueur(porte_monnaie)
        # début du jeu
        j=1
        while j != 0 :
                # numéro choisi par le joueur
                numero_mise = joueur1.num_joueur(numero_mise)
                # choisir sa mise
                somme_misee = joueur1.mise_joueur(somme_misee)
                print("\n Votre mise est de {} $ sur le numéro {} \n".format(joueur1.somme_misee, joueur1.numero_mise))
                # lance la roulette
                print("A vos jeux... La roulette est lancée... \n")
                gagne=random.randrange(50)
                print("Le numéro gagnant est le numéro ", gagne)
                # gains
                gain = 0
                jeu = ZCasino_jeu.Jeu(gagne, gain)
                gain = jeu.gain_partie(gagne, joueur1.somme_misee, joueur1.numero_mise, gain)
                # argent restant au joueur
                joueur1.porte_monnaie = joueur1.porte_monnaie + jeu.gain
                print("Il vous reste donc {} $ pour continuer de jouer.".format(joueur1.porte_monnaie))
                # possibilité de rejouer ou non
                if joueur1.porte_monnaie == 0:
                        print("\nVous n'avez plus d'argent ! Au revoir et à bientôt au ZCasino ")
                        j=0
                else:
                        r=input(" Voulez vous rejouer ? (O / N) ")
                        if r == "O" or r == "o" :
                                j=1
                        else:
                                print("Au revoir et à bientôt au ZCasino ")
                                j=0
                                break
except KeyboardInterrupt:
        print("\n")