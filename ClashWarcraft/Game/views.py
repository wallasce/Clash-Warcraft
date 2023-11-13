from django.shortcuts import render
from CharacterSelect.models import characterSelect
from CharacterSelect.views import selectCharacter
from GameSettings.models import GameSettings
from GameSettings.views import modeSelect, factionSelect, InitialPage
from PvESettings.models import PvESetting
from PvESettings.views import setMobs

def userSelectCharacter(request, faction, player):
    playersCharacter = characterSelect.objects.all()

    if playersCharacter[player].tank == '':
        return selectCharacter(request, faction, 'Tank', player)
    elif playersCharacter[player].melee == '':
        return selectCharacter(request, faction, 'Melee', player)
    elif playersCharacter[player].ranged == '':
        return selectCharacter(request, faction, 'Ranged', player)
    elif playersCharacter[player].heal == '':
        return selectCharacter(request, faction, 'Heal', player)
    else:
        return None
    

def game(request):
    # Set Game Settings.
    settings = GameSettings.objects.first() 

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
        settings = PvESetting.objects.first()
        settings.raid += 1
        settings.save()
        
        setMobs()
    