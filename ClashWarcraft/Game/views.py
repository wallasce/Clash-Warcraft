from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from Cards.models import Card
from Cards.views import createCards, deleteCards
from CharacterSelect.models import characterSelect
from CharacterSelect.views import resetTeams
from GameSettings.models import GameSetting
from GameSettings.views import modeSelect, factionSelect, InitialPage, resetSettings, LoadPage, resetLoadScreen
from PvESettings.models import PvESetting
from PvESettings.views import setMobs, resetPve
from .models import Winner
from .wrapper import setParametersGame, setParametersResult, userSelectCharacter, sortCharacters

import json

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
        setMobs()


    winner = Winner.objects.first()
    if (winner.sideWinner == ''):
        if not settings.passLoadScreen:
            return LoadPage(request)
        
        # Create Cards
        createCards()

        # Render Game Screen.
        parameters = setParametersGame()
        return render(request, 'Game/game.html', parameters)
    else:
        parameters = setParametersResult()
        return render(request, 'Game/result.html', parameters)
    
def getCharacterName(request):
    characters1 = characterSelect.objects.first().getCharactersName()
    characters2 = []

    gameMode = GameSetting.objects.first().gameMode
    if (gameMode == 'pvp'):
        characters2 = characterSelect.objects.last().getCharactersName()
    elif(gameMode == 'pve'):
        characters2 = PvESetting.objects.first().getMobsName()
    
    characters = sortCharacters(characters1, characters2)
    
    response = json.dumps({
        'names' : characters,
    })

    return HttpResponse(response)

def getPercentage(request):
    card = request.GET.get('from')
    cardToUpdate = Card.objects.all().filter(Q(characterCard__name = card) | Q(mobCard__name = card)).first()
    percentage = cardToUpdate.getLifeInPercentage()

    response = json.dumps({
        'percentage' : percentage
    })
    return HttpResponse(response)

def getGameMode(request):
    gameSetting = GameSetting.objects.first()

    response = json.dumps({
        'mode' : gameSetting.gameMode
    })

    return HttpResponse(response)

def setWinner(request):
    if (request.method == 'POST'):
        loser = request.body.decode('utf-8') 
        
        winner = Winner.objects.first()
        winner.sideWinner = 'Player 1' if loser == 'right' else 'Player 2'
        winner.save()
        redirect('/game')

    return HttpResponse(request)

def resultRequest(request):
    if (request.method == 'POST'):
        action = request.body.decode('utf-8') 
        if action == 'playAgain':
            resetLoadScreen()
            deleteCards()
            resetWinner()
        elif action == 'main':
            resetSettings()
            resetTeams()
            resetPve()
            deleteCards()
            resetWinner()
        elif action == 'continue':
            resetLoadScreen()
            deleteCards()
            resetWinner()

            settingsPvE = PvESetting.objects.first()
            settingsPvE.raid += 1
            settingsPvE.save()



    return HttpResponse(request)

def resetWinner():
    winner = Winner.objects.first()
    winner.sideWinner = ''
    winner.save()