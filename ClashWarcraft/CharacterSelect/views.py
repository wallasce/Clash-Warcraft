from django.shortcuts import render, HttpResponse
from Character.models import Character
from .models import characterSelect
from .setters import *

def resetTeams() -> None:
    teams = characterSelect.objects.all()
    for team in teams:
        team.tank = ''
        team.melee = ''
        team.ranged = ''
        team.heal = ''
        team.save()

def selectCharacter(request, factionRequired, typeRequired, player):
    backgroundPath = 'CharacterSelect/Image/' + factionRequired + 'Background.jpg'
    characterOptions = Character.objects.all().filter(faction = factionRequired , type = typeRequired)
    
    options = [characterOption.name for characterOption in characterOptions]
    options = []
    for characterOption in characterOptions:
        pathImage = 'Character/Image/' + formatName(characterOption.name) + '.png'
        pathClassImage = 'Character/Image/Class/' + formatName(characterOption.kind) + '.png'
        options.append({
            'name' : characterOption.name,
            'class' : characterOption.kind,
            'pathClassImage': pathClassImage,
            'pathImage' : pathImage,
        })

    parameters = {
        'backgroundPath' : backgroundPath,
        'type' : typeRequired,
        'options' : options,
        'player' : player + 1,
    }

    return render(request, 'CharacterSelect/characterSelect.html', parameters)

def setCharacter(request):
    if (request.method == 'POST'):
        teams = characterSelect.objects.all() 
        character = request.body.decode('utf-8')
        type = Character.objects.all().filter(name = character)[0].type
        
        if (type == 'Tank'):
            setTank(character, teams)
        elif (type == 'Melee'):
            setMelee(character, teams)
        elif (type == 'Ranged'):
            setRanged(character, teams)
        elif (type == 'Heal'):
            setHeal(character, teams)


    return HttpResponse(request)  