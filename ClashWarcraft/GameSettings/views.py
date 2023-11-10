from django.shortcuts import render, HttpResponse

from .models import GameSettings

# Views Functios
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
    return render(request, 'GameSettings/modeSelect.html', parameters)

def factionSelect(request):
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
                'value' : 'horde',
                'path' : pathImageModeSelect + 'horde.png'
            },{
                'value' : 'alliance',
                'path' : pathImageModeSelect + 'alliance.png'
            }
        ]
    }

    return render(request, 'GameSettings/factionSelect.html', parameters)

def InitialPage(request):
    return render(request, 'GameSettings/initialScreen.html')

# API Functions
def resetSettings():
    settings = GameSettings.objects.first() 
    settings.passHomeScreen = False
    settings.gameMode = ""
    settings.faction = ""
    settings.save()

def passInitialScreen(request):
    if (request.method == 'POST'):
        settings = GameSettings.objects.first() 
        settings.passHomeScreen = True
        settings.save()

    return HttpResponse(request)  

def setGameMode(request):
    if (request.method == 'POST'):
        settings = GameSettings.objects.first() 
        settings.gameMode = request.body.decode('utf-8')
        settings.save()

    return HttpResponse(request)

def setFaction(request):
    if (request.method == 'POST'):
        settings = GameSettings.objects.first()
        settings.faction = request.body.decode('utf-8')
        settings.save()

    return HttpResponse(request)
