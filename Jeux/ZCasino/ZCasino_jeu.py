class Jeu:
    """Classe définissant le jeu de la roulette caractérisé par :
    - un numéro gagnant ;
    - un gain rapporté    """

    
    def __init__(self, gagne, gain):
        """Constructeur de notre classe"""
        self.gagne = gagne
        self.gain = gain

    import random
    def num_gagnant(self, gagne):
        """Méthode permettant de selectionner le numéro gagnant   """
        self.gagne = random.randrange(50)
        print("Le numéro gagnant est le numéro ", self.gagne)
        
    import math
    def gain_partie(self, gagne, somme_misee, numero_mise, gain):
        """Méthode permettant de déterminer le gain du joueur en fonction du numéro gagnant  """
        import math
        if gagne != numero_mise :
            if (self.gagne %2 == 0 and numero_mise %2 == 0) or (gagne %2 != 0 and numero_mise %2 != 0):
                self.gain = math.ceil(somme_misee * 0.5)
                print("\n Vous avez misé sur la bonne couleur, vous gagnez {} $".format(self.gain))
            else:
                print("\n Loupé, Vous venez de perdre votre mise !")
                self.gain = -somme_misee                
        else:
            self.gain = 3 * somme_misee
            print("\n Votre gain est de 3 fois votre mise, soit {} $".format(self.gain))
