import json

def jsontoini(sourcefilepath, destinationfilepath):
  filecontent = open(sourcefilepath).read()
  jsoninput = json.loads(filecontent)

  headers = ''
  body = ''

  for i in range(len(jsoninput)):
    keys = list(jsoninput[i])
    for j in range(len(keys)): 
      if headers.find(keys[j]) == -1 : 
        headers += keys[j]
        if j < len(keys) - 1 : headers += ','  
      body += str(jsoninput[i].get(keys[j])) + ',' if j < len(keys) - 1 else str(jsoninput[i].get(keys[j])) + '\n'

  csvcontent = headers + '\n' + body
  print(csvcontent)
    

  if (len(csvcontent) <= 0) :
    return "Aucun contenu n'a pu être lu."

  file = open(destinationfilepath, 'w')
  file.write(csvcontent)
  file.close()

  return 'Fichier converti avec succès, enregistré sur le chemin : ' + destinationfilepath


sourcepath = input('Chemin du fichier JSON à convertir : ')
destinationpath = input('Chemin de destination du fichier CSV : ')

print(jsontoini(sourcepath, destinationpath))