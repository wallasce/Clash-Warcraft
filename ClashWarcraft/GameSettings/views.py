from django.shortcuts import render, HttpResponse
from .models import GameSetting

# Views Functios
def modeSelect(request):
    pathImageModeSelect = 'GameSettings/Image/ModeSelect/'

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
    return render(request, 'GameSettings/modeSelect.html', parameters)

def factionSelect(request):
    pathImageModeSelect = 'GameSettings/Image/FactionSelect/'

    settings = GameSetting.objects.first() 
    if (settings.gameMode == 'pvp'):
        backgroundImage = pathImageModeSelect + 'pvpBackground.jpg'
    elif (settings.gameMode == 'pve'):
        backgroundImage = pathImageModeSelect + 'pveBackground.jpg'

    parameters = {
        'backgroundPath' : backgroundImage,
        'factions' : [
            {
                'value' : 'Horde',
                'path' : pathImageModeSelect + 'horde.png'
            },{
                'value' : 'Alliance',
                'path' : pathImageModeSelect + 'alliance.png'
            }
        ]
    }

    return render(request, 'GameSettings/factionSelect.html', parameters)

def InitialPage(request):
    return render(request, 'GameSettings/initialScreen.html')

# API Functions
def resetSettings():
    settings = GameSetting.objects.first() 
    settings.passHomeScreen = False
    settings.gameMode = ""
    settings.faction = ""
    settings.save()

def passInitialScreen(request):
    if (request.method == 'POST'):
        settings = GameSetting.objects.first() 
        settings.passHomeScreen = True
        settings.save()

    return HttpResponse(request)  

def setGameMode(request):
    if (request.method == 'POST'):
        settings = GameSetting.objects.first() 
        settings.gameMode = request.body.decode('utf-8')
        settings.save()

    return HttpResponse(request)

def setFaction(request):
    if (request.method == 'POST'):
        settings = GameSetting.objects.first()
        settings.faction = request.body.decode('utf-8')
        settings.save()

    return HttpResponse(request)
