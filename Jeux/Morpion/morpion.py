
import numpy as np
grille = np.zeros((3,3))



jIa = 1
jHumain = 2
nbparties = 0
score1, score2 = 0,0
currentplayer = jIa





def AfficherGrille(g):
	print()
	for i in range(3):
		print('|',end='')   
		for j in range(3): 
            
			if g[i][j] == 1:
				print(' ❌ |',end='')
			elif g[i][j] == 2:
				print(' ⭕ |',end='')
			else:
				print(' . |',end='')
		print()
    
def Terminal_Test(g): 
    
    # On compte au préalable le nombre de case rempli 
    compteur = 0
    for i in range(3):
        for j in range(3):
            if g[i][j] != 0:
                compteur += 1
    
    # scan diagonale decroissante
    if (g[0][0]==g[1][1]==g[2][2] and g[0][0]!=0):
        return True,g[0][0],compteur #fin de jeu, retour du gagnant
    # scan diagonale croissante
    elif (g[0][2]==g[1][1]==g[2][0] and g[0][2]!=0):
        return True, g[0][2],compteur #fin de jeu, retour du gagnant
        
    else:
        for i in range(3):
            # scan horizontales
            if (g[i][0]==g[i][1]==g[i][2] and g[i][0]!=0):
                return True, g[i][0],compteur #fin de jeu, retour du gagnant
            # scan verticales    
            elif (g[0][i]==g[1][i]==g[2][i] and g[0][i]!=0):
                return True, g[0][i],compteur #fin de jeu, retour du gagnant
    
    

    # Si toutes la grille est rempli           
    if compteur == 9:
        return True, 'Pas de gagnant',compteur #fin de jeu, match nul
    
    # Si on arrive à cette partie du code, cela voudrait dire que personne n'a encore aligné 3 pion, et il n'y a pas mathnul, ainsi on continue de jouer
    return False, 'Pas de gagnant',compteur

Terminal_Test(grille)


def Utility(g):
    findejeu,gagnant,caserestante=Terminal_Test(g)
    global jIa,jHumain
    if findejeu:
        if gagnant == jIa:
            val = 1 + caserestante
        elif gagnant == jHumain:
            val = -1 * (1 + caserestante)
        else:
            val = 0
        return val


def Actions(g): 
                 
    #s Si le jeu n'est pas fini    
    if Terminal_Test(g)[0] == False:
        actions=[] 
        for i in range(3):
            for j in range(3):
                if (g[i][j] == 0): # si la case est vide
                    actions.append((i,j))
    
        return actions
Actions(grille)

def Result(g,pos):   #place un element à la position pos dans la grille g
    global currentplayer,jIa,jHumain

    if Terminal_Test(g)[0] != True: # si la partie n'est pas fini
        if pos in Actions(g): # si l'action demandé est possible
            (x,y)=pos
            g[x][y] = currentplayer # on pose le pio du joueur sur la grille

        ## on passe au joueur suivant  
        if currentplayer==jIa:
            currentplayer=jHumain
        elif currentplayer==jHumain:
            currentplayer=jIa 
        return g # on retourne la nouvelle grille



kkk = 0
def min_max_value(grille, prof, maxi):
	global kkk
	kkk += 1
	if Terminal_Test(grille)[0]: # si l'etat du jeu est une partie fini alors
		return Utility(grille)
    
#	print("-- *mmvalue* MAXI {} // PROF {} // TERMINAL-TEST {} // UTILITY {}".format(maxi, prof,Terminal_Test(grille)[0],Utility(grille)))
	if maxi:
		meilleurscore=-1000
		
		actionspossible = Actions(grille)
		
		#print("...",actionspossible)
		for (i,j) in actionspossible:
			grille[i][j]=jIa
			#AfficherGrille(grille)
			#print(i,j)
			score = min_max_value(grille, prof+1, False)
			grille[i][j] = 0
			meilleurscore = max([score,meilleurscore])
			#print("##################### *mmvalue* SCORE {}".format(meilleurscore))
		return meilleurscore
	
	else:
		meilleurscore = 1000
		for i in range(3):
			for j in range(3):
				if grille[i][j]==0:
					grille[i][j]=jHumain
					score = min_max_value(grille, prof+1, True)
					grille[i][j]=0
					meilleurscore = min([score,meilleurscore])
		return meilleurscore

min_max_value(grille, 100, True)

def MiniMax_Decision(grille):
    global currentplayer
    meilleurscore=-1000
    for i in range(3):
        for j in range(3):
            if grille[i][j]== 0: #si la grille est vide
                grille[i][j]= jIa #on pose le pion
                score = min_max_value(grille, 0, False)
                grille[i][j] = 0
                if score > meilleurscore:
                    meilleurscore = score
                    decision = (i,j)
    grille[decision[0]][decision[1]]=jIa
    currentplayer=jHumain
    return grille

def Jeu(g):
    
    global currentplayer, grille, score1,score2,nbparties
	# Si GAME OVER
    if (Terminal_Test(g)[0]==True and Actions(g)==None):
        nbparties += 1
        print( " ----------------------- fin de partie -- Nb de Parties : {}".format(nbparties))
        
        winneur = Terminal_Test(g)[1]
        if (winneur == 1):
            text = ' > Ia gagne !'
            score1 += 1
        elif (winneur == 2):
            text = ' > Vous avez gagnez '
            score2 += 1
        else:
            winneur = currentplayer
            text = ' > match nul'
	   
        print(text)

        print("Score de l'ia : ", score1)
        print("Score du joueur : ", score2)
        print()
        choix = -5
        while (choix!=1 and choix!=0):
            choix=int(input("Voulez-vous rejouer ? \n (0 : NON)  (1 : OUI) : "))

        if choix==1:
            print('\n ************************************* \n')
            grille = np.zeros((3,3))
            currentplayer=winneur
            if currentplayer == jHumain:
                 AfficherGrille(grille)
            Jeu(grille)
        else:
            return print("Merci à la prochaine !")
        
	# 
    elif (Terminal_Test(g)[0]!=True) :
        if currentplayer == jIa:
            print("\n Morpheus joue...")
            g=MiniMax_Decision(grille)
            #s=MiniMax_Decision_AB()
            print(" ----------------------- Morpheus a joué.")
            AfficherGrille(g)
            Jeu(g)
            
        if currentplayer == jHumain:
            #print("KKK",kkk)
            l=Actions(g)
            if l!=None:
                print('Actions possibles : ' + str(l))
                a=int(input('choix colonne : '))
                b=int(input('choix ligne : '))
                while(((a,b) not in l ) or (type(a) != int) or (type(b) != int)):
                    print("Oops, vos coordonnées ne sont pas valides... essayez a nouveau !")
                    a=int(input('choix LIGNE 1 : '))
                    b=int(input('choix COLONNE 2 : ')) 
                Result(g,(a,b))
                currentplayer=jIa
                Jeu(g)
                
try:                
    print('**** MORPION - HUMAN vs MORPHEUS ****')
    Jeu(grille)
except KeyboardInterrupt:
     print("\n")