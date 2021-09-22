import random

def checknumber(number, targetnumber):
  if (number == targetnumber):
    print('Gagné !')
    return True
  elif (number < targetnumber):
    print("C'est plus...")
  elif (number > targetnumber):
    print("C'est moins...")

  return False

def playgame():
  try:
    min = int(input('Entrez le nombre minimal à deviner : '))
    max = int(input('Entrez le nombre maximal à deviner : '))
  except ValueError:
    print("Merci de n'entrer que des nombres.")

  winningnumber = random.randint(min, max)  
  isWin = False

  print('Le chiffre à deviner est compris entre ' + str(min) + ' et ' + str(max) + '.')

  while isWin == False:
    try:
      number = int(input('Quel est le chiffre mystère ? '))
    except ValueError:
      print("Merci de n'entrer que des nombres.")

    isWin = checknumber(number, winningnumber)

  replay = input('Voulez-vous rejouer ? Entrez "oui" pour rejouer ou appuyez sur Entrée pour quitter.')
  if replay == 'oui':
    playgame()

playgame()