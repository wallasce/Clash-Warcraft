from django.shortcuts import render
from GameSettings.models import GameSetting
from GameSettings.views import modeSelect, factionSelect, InitialPage
from PvESettings.models import PvESetting
from PvESettings.views import setMobs
from .wrapper import setParametersGame, userSelectCharacter

def game(request):
    # Set Game Settings.
    settings = GameSetting.objects.first() 

    if not settings.passHomeScreen:
        return InitialPage(request)
    elif settings.gameMode == '':
        return modeSelect(request)
    elif settings.faction == '':
        return factionSelect(request)

    # Player 1 Selection
    faction = settings.faction
    player1 = 0
    userSelect = userSelectCharacter(request, faction, player1)
    if (userSelect):
        return userSelect
    
    # Player 2 Selection If PvP mode, else Computer Selection.
    if (settings.gameMode == 'pvp'):
        player2 = 1
        factionOpposite = 'Horde' if faction == 'Alliance' else 'Alliance'

        userSelect = userSelectCharacter(request, factionOpposite, player2)
        if (userSelect):
            return userSelect
    elif (settings.gameMode == 'pve'):
        settingsPvE = PvESetting.objects.first()
        settingsPvE.raid += 1
        settingsPvE.save()
        
        setMobs()

    # Render Game Screen.
    parameters = setParametersGame()
    return render(request, 'Game/game.html', parameters)
    