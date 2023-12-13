from .models import Card
from Character.models import Character
from Mob.models import Mob

def createCardCharacter(nameCharacters : str) -> None:
    for nameCharacter in nameCharacters:
        character = Character.objects.all().filter(name = nameCharacter)[0]
        Card.objects.create(characterCard = character)

def createCardMob(nameMobs : str) -> None:
    for nameMob in nameMobs:
            mob = Mob.objects.all().filter(name = nameMob)[0]
            Card.objects.create(mobCard = mob)