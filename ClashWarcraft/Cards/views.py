from django.shortcuts import render, HttpResponse
from django.db.models import Q
from .models import Card
from .wrapper import createCardCharacter, createCardMob, deleteAllSkillOfCards, getCardFromName
from Character.models import Character
from CharacterSelect.models import characterSelect
from GameSettings.models import GameSetting
from PvESettings.models import PvESetting

import json

def applySkill(request) :
    requestDict = json.loads(request.body.decode())
    print(requestDict)
    cardName = requestDict['currentCard']
    currentCard = Card.objects.all().filter(Q(characterCard__name = cardName) | Q(mobCard__name = cardName)).first()
    skillNumber = requestDict['skillNumber'] if requestDict['skillNumber'] != 0 else currentCard.skillWithoutCD()
    
    currentCard.applySkill(skillNumber, requestDict['targetCard'])

    return HttpResponse(request)

def isDead(request):
    card = request.GET.get('character')
    cardToCheck = Card.objects.all().filter(Q(characterCard__name = card) | Q(mobCard__name = card)).first()
    isDead = True if cardToCheck.currentStamina == 0 else False

    response = json.dumps({
        'isDead' : isDead
    })
    return HttpResponse(response)

def getCooldowns(request):
    name = request.GET.get('character')
    cardToGet = Card.objects.all().filter(Q(characterCard__name = name) | Q(mobCard__name = name)).first()
    cooldowns = cardToGet.getCooldowns()

    response = {
            'cooldowns' : cooldowns,
        }
    
    response = json.dumps(response)
    return HttpResponse(response)

def reduceCooldown(request):
    requestDict = json.loads(request.body.decode())
    cardName = requestDict['cardName']
    
    cardToReduce = getCardFromName(cardName)
    cardToReduce.reduceAllCooldown()
    return HttpResponse(request)

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
    deleteAllSkillOfCards()
    cards = Card.objects.all()
    for card in cards:
        card.delete()