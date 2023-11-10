from django.shortcuts import render
from GameSettings.models import GameSettings
from GameSettings.views import modeSelect, factionSelect, InitialPage

# Create your views here.
def game(request):
    settings = GameSettings.objects.first() 

    if not settings.passHomeScreen:
        return InitialPage(request)
    elif settings.gameMode == '':
        return modeSelect(request)
    elif settings.faction == '':
        return factionSelect(request)