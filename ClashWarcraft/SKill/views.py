from django.shortcuts import HttpResponse
from .wrapper import getCharacterNames, getPathSkill

import json

def getSkillFromCharacterSelected(request):
    charactersName = getCharacterNames()
    
    response = {}
    for characterName in charactersName:
        response[characterName] = getPathSkill(characterName)

    response = json.dumps(response)
    return HttpResponse(response)
        