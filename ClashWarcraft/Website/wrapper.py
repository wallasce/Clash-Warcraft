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

def getRandomCharacterName() -> str:
    characters = Character.objects.all()
    character = characters[random.randrange(0,len(characters))]
        
    return formatName(character.name)

def getRandomSkills() -> list[str]:
    characters = Character.objects.all()
    character = characters[random.randrange(0,len(characters))]
    
    skills = character.skill.all()
    
    skillsPath = []
    for skill in skills:
        skillsPath.append('Skill/Image/'+ formatName(str(skill)) +'.png')
    skillsPath.append('Game/Image/Icons/cd.png')

    return skillsPath

def getRandomPercentageBarLife() -> str:
    percentage = random.randrange(0,10) * 10

    return str(percentage)

def getRandomPromotion() -> str:
    image = random.randrange(1,5)

    return 'Promotion' + str(image)

def getImageTutorial(theme : str) -> list[str]:
    pathImage = []

    if (theme == 'deadCard'):
        pathImage.append('Game/Image/Cards/Dead.png')
    elif (theme == 'barLife'):
        pathImage.append('Game/Image/Cards/' + getRandomCharacterName() + '.png')
        pathImage.append('Game/Image/Bars/'+ getRandomPercentageBarLife() +'.png')
    elif (theme == 'card'):
        pathImage.append('Game/Image/Cards/' + getRandomCharacterName() + '.png')
    elif (theme == 'abilities'):
        pathImage = getRandomSkills()
    elif (theme == 'end'):
        pathImage.append('Website/Image/GamePlay/TeamDead.png')
    elif (theme == 'promotion'):
        pathImage.append('Website/Image/GamePlay/' + getRandomPromotion() + '.png')

    return pathImage

def getTutorial():
    tutorials = Tutorial.objects.all()

    tutorialSteps = []

    for tutorial in tutorials:
        tutorialSteps.append({
            'title' : tutorial.title,
            'subtitle' : tutorial.subtitle,
            'description' : tutorial.description,
            'stepNumber' : tutorial.step,
            'images' : getImageTutorial(tutorial.theme),
            'background' : 'Website/Image/BackgroundTutorial/' + str(tutorial.step) + '.png',
        })

    data = {
        'tutorialSteps' : tutorialSteps,
    }

    return data