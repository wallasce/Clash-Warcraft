from django.shortcuts import render, HttpResponse
from .models import Card
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
    
    nameCharacters = characterSelect.objects.first().getCharactersName()

    gameMode = GameSetting.objects.first().gameMode
    if (gameMode == 'pvp'):
        nameCharacters += characterSelect.objects.last().getCharactersName()
    elif(gameMode == 'pve'):
        nameCharacters += PvESetting.objects.first().getMobsName()

    for nameCharacter in nameCharacters:
        character = Character.objects.all().filter(name = nameCharacter)[0]
        Card.objects.create(characterCard = character)

    cards = Card.objects.all()
    for card in cards:
        attributes = card.characterCard.attributes
        card.currentArmor = attributes.armor
        card.currentPower = attributes.power
        card.currentStamina = attributes.stamina

        card.save()

def deleteCards() -> None:
    cards = Card.objects.all()
    for card in cards:
        card.delete()