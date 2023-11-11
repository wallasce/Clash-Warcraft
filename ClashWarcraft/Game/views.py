from django.shortcuts import render
from CharacterSelect.models import characterSelect
from CharacterSelect.views import selectCharacter
from GameSettings.models import GameSettings
from GameSettings.views import modeSelect, factionSelect, InitialPage

def game(request):
    # Set Game Settings.
    settings = GameSettings.objects.first() 

    if not settings.passHomeScreen:
        return InitialPage(request)
    elif settings.gameMode == '':
        return modeSelect(request)
    elif settings.faction == '':
        return factionSelect(request)
    
    # Set Character.
    playersCharacter = characterSelect.objects.all()
    faction = settings.faction

    # Player 1
    player1 = 0
    if playersCharacter[player1].tank == '':
        return selectCharacter(request, faction, 'Tank')
    elif playersCharacter[player1].melee == '':
        return selectCharacter(request, faction, 'Melee')
    elif playersCharacter[player1].ranged == '':
        return selectCharacter(request, faction, 'Ranged')
    elif playersCharacter[player1].heal == '':
        return selectCharacter(request, faction, 'Heal')