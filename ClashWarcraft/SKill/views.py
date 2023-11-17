from django.shortcuts import HttpResponse
from .wrapper import getCharacterNames, getPathSkill

def getSkillFromCharacterSelected(request):
    charactersName = getCharacterNames()
    
    response = {}
    for characterName in charactersName:
        response[characterName] = getPathSkill(characterName)
    
    return HttpResponse(response)
        