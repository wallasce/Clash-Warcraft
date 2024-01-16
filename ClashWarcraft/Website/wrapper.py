from Character.models import Character

def formatName(name : str):
    formatedName = name.replace("'", "")
    formatedName = formatedName.replace(" ", "")
    return formatedName

def getCharacterParameters(faction : str):
    characters = Character.objects.all().filter(faction = faction)

    characterParameters = []

    for character in characters:
        characterParameters.append({
            'name' : character.name,
            'pathImg' : 'Website/Image/Characters/' + formatName(character.name) + '.jpeg',
        })

    return characterParameters

def getCharacterDetails(name : str):
    character = Character.objects.all().filter(name = name)[0]
    details = {
        'name' : name,
        'backgroundPath' : 'Website/Image/BackgroundClass/' + formatName(character.kind) + '.avif',
    }

    return details