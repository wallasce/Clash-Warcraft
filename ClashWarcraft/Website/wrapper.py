from Character.models import Character

def formatName(name : str):
    return name.replace("'", "")

def getCharacterParameters(faction : str):
    characters = Character.objects.all().filter(faction = faction)

    characterParameters = []

    for character in characters:
        characterParameters.append({
            'name' : character.name,
            'pathImg' : 'Website/Image/Characters/' + formatName(character.name) + '.jpeg',
        })

    return characterParameters