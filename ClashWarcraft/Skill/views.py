from django.shortcuts import HttpResponse
from .wrapper import getCharacterNames, getSkillData

import json

def getSkillFromCharacterSelected(request):
    charactersName = getCharacterNames()
    
    response = {}
    for characterName in charactersName:
        paths, types = getSkillData(characterName)
        response[characterName] = {
            'path' : paths,
            'type' : types,
        }
    response = json.dumps(response)
    return HttpResponse(response)
        