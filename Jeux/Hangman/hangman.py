import pygame
import random

try:
    pygame.init()
    winHeight = 500
    winWidth = 1000
    win=pygame.display.set_mode((winWidth,winHeight))  # Crée une fenêtre de jeu

    # Définition des couleurs
    BLACK = (0,0, 0)
    WHITE = (255,255,255)
    RED = (255,0, 0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    LIGHT_BLUE = (102,255,255)

    # Définition des polices
    btn_font = pygame.font.SysFont("arial", 20)
    guess_font = pygame.font.SysFont("monospace", 24)
    lost_font = pygame.font.SysFont('arial', 45)
<<<<<<< HEAD
=======
    word = ''
    buttons = []
    guessed = []
    hangmanPics = [pygame.image.load('../Jeux/Hangman/hangman0.png'), pygame.image.load('../Jeux/Hangman/hangman1.png'), pygame.image.load('../Jeux/Hangman/hangman2.png'), pygame.image.load('../Jeux/Hangman/hangman3.png'), pygame.image.load('../Jeux/Hangman/hangman4.png'), pygame.image.load('../Jeux/Hangman/hangman5.png'), pygame.image.load('../Jeux/Hangman/hangman6.png')]
>>>>>>> 3e19a71e5d3b5c5ffd355c71485829beb33fd71c

    word = ''  # Mot à deviner
    buttons = []  # Liste des boutons pour les lettres
    guessed = []  # Liste des lettres devinées
    hangmanPics = [pygame.image.load('../Jeux/Hangman/hangman0.png'), pygame.image.load('../Jeux/Hangman/hangman1.png'), pygame.image.load('../Jeux/Hangman/hangman2.png'), pygame.image.load('../Jeux/Hangman/hangman3.png'), pygame.image.load('../Jeux/Hangman/hangman4.png'), pygame.image.load('../Jeux/Hangman/hangman5.png'), pygame.image.load('../Jeux/Hangman/hangman6.png')]

    limbs = 0  # Nombre de parties du pendu déjà dessinées

    def redraw_game_window():
        """Redessine la fenêtre de jeu."""
        global guessed
        global hangmanPics
        global limbs
        win.fill(GREEN)
        
        # Affichage des boutons pour les lettres
        for i in range(len(buttons)):
            if buttons[i][4]:
                pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
                pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2)
                label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
                win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

        spaced = spacedOut(word, guessed)
        label1 = guess_font.render(spaced, 1, BLACK)
        rect = label1.get_rect()
        length = rect[2]
        win.blit(label1,(winWidth/2 - length/2, 400))

        pic = hangmanPics[limbs]
        win.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 150))
        pygame.display.update()

    def randomWord():
<<<<<<< HEAD
        """Choisit un mot aléatoire depuis un fichier."""
=======
>>>>>>> 3e19a71e5d3b5c5ffd355c71485829beb33fd71c
        file = open('../Jeux/Hangman/words.txt')
        f = file.readlines()
        i = random.randrange(0, len(f) - 1)
        return f[i][:-1]

    def hang(guess):
        """Vérifie si la lettre devinée est présente dans le mot."""
        global word
        if guess.lower() not in word.lower():
            return True
        else:
            return False

    def spacedOut(word, guessed=[]):
        """Affiche le mot avec des espaces pour les lettres devinées."""
        spacedWord = ''
        guessedLetters = guessed
        for x in range(len(word)):
            if word[x] != ' ':
                spacedWord += '_ '
                for i in range(len(guessedLetters)):
                    if word[x].upper() == guessedLetters[i]:
                        spacedWord = spacedWord[:-2]
                        spacedWord += word[x].upper() + ' '
            elif word[x] == ' ':
                spacedWord += ' '
        return spacedWord

    def buttonHit(x, y):
        """Vérifie si un bouton pour une lettre est cliqué."""
        for i in range(len(buttons)):
            if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
                if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                    return buttons[i][5]
        return None

    def end(winner=False):
        """Affiche l'écran de fin de partie."""
        global limbs
        lostTxt = "Perdu, Appuie sur n'importe quelle touche pour continuer"
        winTxt = "Gagné!, Appuie sur n'importe quelle touche pour continuer"
        redraw_game_window()
        pygame.time.delay(1000)
        win.fill(GREEN)

        if winner == True:
            label = lost_font.render(winTxt, 1, BLACK)
        else:
            label = lost_font.render(lostTxt, 1, BLACK)

        wordTxt = lost_font.render(word.upper(), 1, BLACK)
        wordWas = lost_font.render('Le mot était ', 1, BLACK)

        win.blit(wordTxt, (winWidth/2 - wordTxt.get_width()/2, 295))
        win.blit(wordWas, (winWidth/2 - wordWas.get_width()/2, 245))
        win.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
        pygame.display.update()
        again = True
        while again:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    again = False
        reset()

    def reset():
        """Réinitialise la partie."""
        global limbs
        global guessed
        global buttons
        global word
        for i in range(len(buttons)):
            buttons[i][4] = True

        limbs = 0
        guessed = []
        word = randomWord()

    #MAINLINE
    increase = round(winWidth / 13)  # Augmentation pour espacer les boutons
    for i in range(26):
        if i < 13:
            y = 40
            x = 25 + (increase * i)
        else:
            x = 25 + (increase * (i - 13))
            y = 85
        buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])

    word = randomWord()
    inPlay = True

    while inPlay:
        redraw_game_window()
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inPlay = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickPos = pygame.mouse.get_pos()
                letter = buttonHit(clickPos[0], clickPos[1])
                if letter != None:
                    guessed.append(chr(letter))
                    buttons[letter - 65][4] = False
                    if hang(chr(letter)):
                        if limbs != 5:
                            limbs += 1
                        else:
                            end()
                    else:
                        if spacedOut(word, guessed).count('_') == 0:
                            end(True)

    pygame.quit()
except pygame.error:
    print("Erreur pygame.")
