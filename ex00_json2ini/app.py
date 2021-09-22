import json

def jsontoini(sourcefilepath, destinationfilepath):
  filecontent = open(sourcefilepath).read()
  lines = filecontent.split()

  jsoncontent = {}
  
  currenttitle = 'Settings'
  currentobject = {}

  for i in range(0, len(lines)):
    if (lines[i].find('[') == 0 and lines[i].find(']') == len(lines[i]) - 1):
      if len(currentobject) > 0 : 
        jsoncontent[currenttitle] = currentobject
        currentobject = {}
      currenttitle = lines[i][1:len(lines[i]) - 1]

    elif (lines[i].find('#') != 0) and (lines[i].find('=') > 0):
      jsonvalue = lines[i].split('=')
      currentobject[jsonvalue[0]] = jsonvalue[1]

    if (i == len(lines) - 1): 
      jsoncontent[currenttitle] = currentobject

  if (len(jsoncontent) <= 0) :
    return "Aucun contenu n'a pu être lu."

  with open(destinationfilepath, 'w') as outputfile:
    json.dump(jsoncontent, outputfile)

  return 'Fichier converti avec succès, enregistré sur le chemin : ' + destinationfilepath


sourcepath = input('Chemin du fichier ini à convertir : ')
destinationpath = input('Chemin de destination du fichier JSON : ')

print(jsontoini(sourcepath, destinationpath))