from django.db.models.manager import BaseManager

from Character.models import Character

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