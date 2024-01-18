from django.db.models.manager import BaseManager

from Character.models import Character
from Game.models import Lore

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
            'pathImg' : 'Website/Image/Characters/' + formatName(character.name) + '.jpeg',
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
        'role' : character.type,
        'class' : character.kind,
        'skills' : getSkillDetails(character),
        'backgroundPath' : 'Website/Image/BackgroundClass/' + formatName(character.kind) + '.avif',
        'charImagePath' : 'Website/Image/CharactersPNG/' + formatName(character.name) + '.png',
    }

    return details

def getLoreData():
    lores = Lore.objects.all()
    loresData = []

    for lore in lores:
        loresData.append({
            'title' : lore.title,
            'subtitle' : lore.subtitle,
            'heading' : lore.heading,
            'subheading' : lore.subheading,
            'description' : lore.description,
            'raid' : lore.raid,
            'loreImg' : 'Website/Image/Lore/' + str(lore.raid) + '.jpg',
            'buttonPath' : 'Website/Image/LoreButtons/'+ str(lore.raid) + '.png',
            'loreBackground' : 'Website/Image/BackgroundLore/' + str(lore.raid) + '.png',
        })

    details = {
        'loresData' : loresData,
    }
    
    return details