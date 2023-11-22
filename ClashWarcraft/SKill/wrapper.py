from Character.models import Character
from CharacterSelect.models import characterSelect

def getCharacterNames() -> list[str]:
    characters = characterSelect.objects.all()
    characterName = []

    for character in characters:
        names = character.getCharactersName()
        if (names):
            characterName += names

    return characterName

def getSkillData(characterName : str) -> list[str]:
    characterSkills = Character.objects.all().filter(name = characterName)[0].getSkillInformate()
    
    paths = []
    types = []
    for skill in characterSkills:
        paths.append('/static/Skill/Image/'+ skill[0].replace(' ', '') + '.png')
        types.append(skill[1])

    return paths, types