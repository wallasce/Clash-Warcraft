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

def getPathSkill(characterName : str) -> list[str]:
    characterSkills = Character.objects.all().filter(name = characterName)[0].getSkillNames()
    
    paths = []
    for skill in characterSkills:
        paths.append('Skill/Image/'+ skill.replace(' ', '') + '.png')

    return paths