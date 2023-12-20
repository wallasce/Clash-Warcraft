from django.shortcuts import render, HttpResponse
from .models import GameSetting
from .wrapper import getLocalToTravel

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

def LoadPage(request):
    settings = GameSetting.objects.first() 
    
    pathImageModeSelect = 'GameSettings/Image/LoadScreen/'
    extensionJPG = 'Wait.jpg'
    gameMode = settings.gameMode
    if (gameMode == 'pvp'):
        backgroundImage = pathImageModeSelect + gameMode +extensionJPG
    elif (gameMode == 'pve'):
        backgroundImage = pathImageModeSelect + settings.faction +extensionJPG

    local = getLocalToTravel(gameMode)

    parameters = {
        'backgroundPath' : backgroundImage,
        'local' : local,
    }
    return render(request, 'GameSettings/loadScreen.html', parameters)


# API Functions
def resetSettings():
    settings = GameSetting.objects.first() 
    settings.passHomeScreen = False
    settings.gameMode = ""
    settings.faction = ""
    settings.passLoadScreen = False
    settings.save()

def resetLoadScreen():
    settings = GameSetting.objects.first() 
    settings.passLoadScreen = False
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

def passLoadScreen(request):
    if (request.method == 'POST'):
        settings = GameSetting.objects.first()
        settings.passLoadScreen = True
        settings.save()

    return HttpResponse(request)

