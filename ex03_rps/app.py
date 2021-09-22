import random

rps = {
  'pierre': 'feuille', 
  'feuille': 'ciseaux', 
  'ciseaux': 'pierre'
}
rounds = 3

def getcomputerplay():
  play = random.choice(list(rps))
  print("L'ordinateur a joué " + play)
  return play

def getuserplay():
  play = 0  

  print("C'est à vous de jouer !")
  print('1: Pierre | 2: Feuille | 3: Ciseaux')
  while play == 0:
    try:
      playerchoice = int(input('Entrez votre choix : '))
    except ValueError:
      print('Merci de renseigner un chiffre entre 1 et 3.')
    
    if (playerchoice >= 1) and (playerchoice <= 3):
      play = playerchoice
    else:
      print('Merci de renseigner un chiffre entre 1 et 3.')

  return list(rps)[play - 1]
  
def playgame():
  userscore = 0
  computerscore = 0
  isWin = False

  while (isWin == False):
    userplay = getuserplay()
    computerplay = getcomputerplay()

    if (rps.get(userplay) == computerplay):
      computerscore += 1
      print("L'ordinateur remporte la manche !")
    elif (rps.get(computerplay) == userplay):
      userscore += 1
      print("Vous remportez la manche !")
    elif (userplay == computerplay):
      print("Égalité !")
  
    if userscore == 3 or computerscore == 3:
      isWin = True

  if userscore == rounds : 
    print('Vous avez gagné !') 
  elif computerscore == rounds :  
    print("L'ordinateur a gagné")

  replay = input('Voulez-vous rejouer ? Entrez "oui" pour rejouer ou appuyez sur Entrée pour quitter.')
  if replay == 'oui':
    playgame()

print('Bienvenue au jeu du pierre feuille ciseaux !')
playgame()