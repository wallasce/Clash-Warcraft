from django.db.models.manager import BaseManager

from .models import Card, skillOfCard
from Cards.models import Card
from Character.models import Character
from Mob.models import Mob
from Skill.models import Skill

def createCardCharacter(nameCharacters : str) -> None:
    for nameCharacter in nameCharacters:
        character = Character.objects.all().filter(name = nameCharacter)[0]
        cardCharacter = Card.objects.create(characterCard = character)
        createSkillCardCharacter(cardCharacter)

def createCardMob(nameMobs : str) -> None:
    for nameMob in nameMobs:
        mob = Mob.objects.all().filter(name = nameMob)[0]
        cardMob = Card.objects.create(mobCard = mob)
        createSkillCardMob(cardMob)

def addSKillOnCard(card : Card, skills : BaseManager[Skill]) -> None:
    for skill in skills:
        newSkill = skillOfCard(skill = skill, remainingCooldown = skill.cooldown)
        newSkill.save()
        
        card.skills.add(newSkill)
        card.save()

def createSkillCardMob(card : Card) -> None:
    mobName = card.mobCard.name
    skills = Skill.objects.all().filter(skillOff = mobName)
    addSKillOnCard(card, skills)

def createSkillCardCharacter(card : Card) -> None:
    kind = card.characterCard.kind
    specialCharacter = ['Warrior', 'Paladin', 'Death Knight']

    if kind in specialCharacter:
        kind += ' ' + card.characterCard.type
    
    skills = Skill.objects.all().filter(skillOff = kind)
    addSKillOnCard(card, skills)

def deleteAllSkillOfCards() -> None:
    skills = skillOfCard.objects.all()
    for skill in skills:
        skill.delete()