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

def getRandomCharacterName() -> str:
    characters = Character.objects.all()
    character = characters[random.randrange(0,len(characters))]
        
    return formatName(character.name)

def getRandomSkillName() -> str:
    characters = Character.objects.all()
    character = characters[random.randrange(0,len(characters))]
    skill = random.randrange(1,4)
    
    print(character.type)
    if(character.type in ['Melee', 'Tank']):
        return formatName(character.kind) + character.type + str(skill)

    return formatName(character.kind) + str(skill)

def getImageTutorial(theme : str) -> str:
    pathImage = ''

    if (theme == 'deadCard'):
        pathImage = 'Game/Image/Cards/Dead.png'
    elif (theme == 'barLife'):
        pathImage = 'Game/Image/Bars/80.png'
    elif (theme == 'card'):
        pathImage = 'Game/Image/Cards/' + getRandomCharacterName() + '.png'
    elif (theme == 'abilities'):
        pathImage = 'Skill/Image/' + getRandomSkillName() +'.png'
    
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
            'image' : getImageTutorial(tutorial.theme),
            'background' : 'Website/Image/BackgroundTutorial/' + str(tutorial.step) + '.png',
        })

    data = {
        'tutorialSteps' : tutorialSteps,
    }

    return data