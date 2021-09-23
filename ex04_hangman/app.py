import random
from os import system, name
from words import *

def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

def gethiddenword(word, letters):
  hiddenword = ''

  for i in range(0, len(word)):
    hiddenword += word[i] + ',' if word[i] in letters else '_,' 

  return hiddenword


maxtries = 8

def playgame():
  isWin = False
  tries = 0
  letters = []
  word = random.choice(english_words)

  clear()
  print(gethiddenword(word, letters) + ' ' + word)

  while tries != maxtries:
    letter = input('Choisir une lettre : ')
    letters.append(letter)

    if str(letter) not in word:
      tries += 1

    clear()
    
    hiddenword = gethiddenword(word, letters)
    if (hiddenword.find('_') == -1) :
      isWin == True
      tries == maxtries
    else :
      print(hiddenword)

  clear()

  if (isWin == True):
    print('Vous avez gagné ! Le mot était bien ' + word)
  else :
    print('Vous avez perdu... le mot était ' + word)

  replay = input('Voulez-vous rejouer ? Entrez "oui" pour rejouer ou appuyez sur Entrée pour quitter.')
  if replay == 'oui':
    playgame()

print('Bienvenue au jeu du pendu.')
playgame()



# Write a program where the user will have to guess an alphabet completing a word and have a limited number of chances to guess a letter.