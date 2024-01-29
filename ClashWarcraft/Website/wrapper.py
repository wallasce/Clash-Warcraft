from django.db.models.manager import BaseManager
import random

from Character.models import Character
from Game.models import Lore, Tutorial

def formatName(name : str):
    formatedName = name.replace("'", "")
    formatedName = formatedName.replace(" ", "")
    return formatedName

def getCharacterParameters(faction : str):
    characters = Character.objects.all().filter(faction = faction)

    characterParameters = []

    for character in characters:
        characterParameters.append({
            'name' : character.name,
            'pathImg' : 'Website/Image/Characters/' + formatName(character.name) + '.png',
        })

    return characterParameters

def getSkillDetails(character : BaseManager[Character]):
    skillsDetails = []
    skills = character.skill.all()
    for skill in skills:
        skillsDetails.append({
            'name' : skill.name,
            'description' : skill.description,
            'cooldown' : skill.cooldown,
            'imagePath' : '/Skill/Image/'+ str(skill).replace(' ', '') + '.png',
        })

    return skillsDetails

def getCharacterDetails(name : str):
    character = Character.objects.all().filter(name = name)[0]
    details = {
        'name' : name,
        'title' : character.title,
        'story' : character.story,
        'role' : character.type,
        'class' : character.kind,
        'skills' : getSkillDetails(character),
        'attributes' : character.attributes.getAttributes(),
        'classIconPath' : 'Website/Image/ClassIcons/' + formatName(character.kind) + '.png',
        'backgroundPath' : 'Website/Image/BackgroundClass/' + formatName(character.kind) + '.avif',
        'charImagePath' : 'Website/Image/CharactersTransparent/' + formatName(character.name) + '.png',
    }

    return details