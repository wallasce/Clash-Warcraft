from django.shortcuts import render, HttpResponse
from .models import Card
from .wrapper import createCardCharacter, createCardMob
from Character.models import Character
from CharacterSelect.models import characterSelect
from GameSettings.models import GameSetting
from PvESettings.models import PvESetting

import json

def applySkill(request) :
    requestDict = json.loads(request.body.decode())
    currentCard = Card.objects.all().filter(characterCard__name = requestDict['currentCard'])[0]
    currentCard.applySkill(requestDict['skillNumber'], requestDict['targetCard'])

    return HttpResponse(request)

def isDead(request):
    cardToCheck = Card.objects.all().filter(characterCard__name = request.GET.get('character')).first()
    isDead = True if cardToCheck.currentStamina == 0 else False

    response = json.dumps({
        'isDead' : isDead
    })
    return HttpResponse(response)

def createCards() -> None:
    count = Card.objects.count()
    if (count == 8):
        return
    elif (count > 0):
        deleteCards()

    # Create Cards to Player 1.
    namesPlayer1Character = characterSelect.objects.first().getCharactersName()
    createCardCharacter(namesPlayer1Character)
    
    gameMode = GameSetting.objects.first().gameMode
    # Create Cards to Player 2 or Mobs to Computer.
    if (gameMode == 'pvp'):
        namesPlayer2Character = characterSelect.objects.last().getCharactersName()
        createCardCharacter(namesPlayer2Character)
    elif(gameMode == 'pve'):
        nameMobs = PvESetting.objects.first().getMobsName()
        createCardMob(nameMobs)

    # Initialize Cards.
    cards = Card.objects.all()
    for card in cards:
        card.initialize()
        card.save()

def deleteCards() -> None:
    cards = Card.objects.all()
    for card in cards:
        card.delete()