from django.shortcuts import render
from Character.models import Character
from .models import characterSelect

def selectCharacter(request, factionRequired, typeRequired):
    backgroundPath = 'CharacterSelect/Image/' + factionRequired + 'Background.jpg'
    characterOptions = Character.objects.all().filter(faction = factionRequired.capitalize() , type = typeRequired)
    
    options = [characterOption.name for characterOption in characterOptions]
    options = []
    for characterOption in characterOptions:
        path = 'Character/Image/' + characterOption.name + '.png'
        options.append({
            'value' : characterOption.name,
            'path' : path
        })

    parameters = {
        'backgroundPath' : backgroundPath,
        'type' : typeRequired,
        'options' : options,
    }

    return render(request, 'CharacterSelect/characterSelect.html', parameters)