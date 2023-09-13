class Joueur:
    """Classe définissant un joueur de roulette caractérisé par :
    - son pseudo ;
    - son porte monnaie ;
    - un numéro misé
    - une somme misée   """

    
    def __init__(self, pseudo, porte_monnaie, numero_mise, somme_misee):
        """Constructeur de notre classe"""
        self.pseudo = pseudo
        self.porte_monnaie = porte_monnaie
        self.numero_mise = numero_mise
        self.somme_misee = somme_misee

    def nom_joueur(self, pseudo):
        """Méthode permettant de vérifier que le nom du joueur n'est pas un chiffre et de l'afficher   """
        NomCorrect = False
        while NomCorrect == False :
            self.pseudo = input("Quel est votre nom ?")
            #self.pseudo = 'Anonyme' if len(self.pseudo) == 0 else self.pseudo
            try:
                int(self.pseudo) != False
            except ValueError:
                print("Bienvenue {} sur la table de la Roulette du Zcasino !".format(self.pseudo))
                NomCorrect = True
            else :
                print("Il y a une erreur, êtes vous certain de votre frappe ?")



    def argent_joueur(self, porte_monnaie):
        """Méthode permettant de vérifier que le joueur a de l'argent pour jouer"""
        Argent = False
        while Argent == False :
            self.porte_monnaie = input("\nAvec quelle somme d'argent souhaitez vous jouer ? ")
            try:
                int(self.porte_monnaie) != False
            except ValueError:
                print("Il y a une erreur, êtes vous certain de votre frappe ?")
            else :
                self.porte_monnaie = int(self.porte_monnaie)
                if self.porte_monnaie < 1 :
                    print("Vous ne pouvez pas jouer sans argent !")
                else :
                    Argent = True

    def num_joueur(self, numero_mise):
        """Méthode permettant de vérifier que le joueur a bien misé sur un numéro de la roulette"""
        Numero = False
        while Numero == False :
            self.numero_mise = input("\nSur quel numéro souhaitez vous miser (entre 0 et 49) ? : ")
            try:
                int(self.numero_mise) != False
            except ValueError:
                print("Il y a une erreur, êtes vous certain de votre frappe ?")
            else :
                self.numero_mise = int(self.numero_mise)
                if self.numero_mise < 0 or self.numero_mise > 49:
                    print("Le numéro choisi n'existe pas, veuillez en choisir un autre !")
                else :
                    Numero = True
    
    def mise_joueur(self, somme_misee):
        """ Methode permettant de vérifier que le joueur mise l'argent qu'il a dans son porte monnaie """
        Mise = False
        while Mise == False :
            self.somme_misee = input("\nQuelle somme souhaitez vous miser sur ce numéro ? : ")
            try:
                int(self.somme_misee) != False
            except ValueError :
                print("Etes vous certain de votre frappe ?")
            else :
                self.somme_misee = int(self.somme_misee)
                if self.somme_misee < 0:
                    print("Vous ne pouvez pas miser un nombre négatif !")
                elif self.somme_misee > self.porte_monnaie:
                    print("Vous n'avez pas assez d'argent !")
                else :
                    Mise = True
