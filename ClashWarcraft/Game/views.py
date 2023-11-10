from django.shortcuts import render
from GameSettings.models import GameSettings

# Create your views here.
def modeSelect(request):
    pathImageModeSelect = 'Game/Image/ModeSelect/'

    parameters = {
        'types' : [
            {
                'value' : 'pvp',
                'path' : pathImageModeSelect + 'pvp.png',
            },{
                'value' : 'pve',
                'path' : pathImageModeSelect + 'pve.png',
            },
        ]        
    }
    return render(request, 'Game/modeSelect.html', parameters)

def game(request):
    pathImageModeSelect = 'Game/Image/FactionSelect/'

    settings = GameSettings.objects.first() 
    if (settings.gameMode == 'pvp'):
        backgroundImage = pathImageModeSelect + 'pvpBackground.jpg'
    elif (settings.gameMode == 'pve'):
        backgroundImage = pathImageModeSelect + 'pveBackground.jpg'

    parameters = {
        'backgroundPath' : backgroundImage,
        'factions' : [
            {
                'value' : 'alliance',
                'path' : pathImageModeSelect + 'alliance.png'
            },{
                'value' : 'horde',
                'path' : pathImageModeSelect + 'horde.png'
            }
        ]
    }

    return render(request, 'Game/factionSelect.html', parameters)