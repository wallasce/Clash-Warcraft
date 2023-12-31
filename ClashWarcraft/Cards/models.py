from django.db import models
from django.db.models import Q
from Character.models import Character
from Mob.models import Mob
from Skill.models import Skill

class skillOfCard(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)
    remainingCooldown = models.IntegerField(blank = True, default = 0)
    effectOn = models.CharField(max_length=50, blank=True)
    remainingEffect = models.IntegerField(blank = True, default = 0)

    def __str__(self) -> str:
        return self.skill.skillOff + "'s Skill Card " + str(self.skill.level)
    
    def reduceCooldown(self) -> None:
        self.remainingCooldown -= 1 if self.remainingCooldown > 0 else 0
        self.save()

    def updateCooldown(self) -> None:
        self.remainingCooldown = self.skill.cooldown
        self.save()

    def updateEffect(self, cardName : str) -> None:
        self.effectOn = cardName
        self.remainingEffect = self.skill.durationEffect
        self.save()

    def reduceEffect(self) -> None:
        self.remainingEffect -= 1 if self.remainingEffect > 0 else 0

        if (self.remainingEffect == 0 and self.effectOn != ''):
            target = self.effectOn
            card = Card.objects.all().filter(Q(characterCard__name = target) | Q(mobCard__name = target)).first()
            self.removeEffect(card)
            self.effectOn = ''

        self.save()

    def removeEffect(self, card) -> None:
        if (self.skill.type == 'Power Buff'):
            card.currentPower -= self.skill.baseEffect
        elif (self.skill.type == 'Armor Buff'):
            card.currentArmor -= self.skill.baseEffect
        card.save()
    
class Card(models.Model):
    characterCard = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)
    mobCard = models.ForeignKey(Mob, on_delete=models.CASCADE, null=True)
    currentArmor = models.FloatField(blank=True, default=0)
    currentPower = models.FloatField(blank=True, default=0)
    currentStamina = models.FloatField(blank=True, default=0)
    skills = models.ManyToManyField(skillOfCard, blank=True)

    def __str__(self) -> str:
        if (self.characterCard):
            return 'Card of ' + self.characterCard.name
        elif (self.mobCard):
            return 'Card of ' + self.mobCard.name
    
    def initialize(self) -> None:
        if (self.characterCard):
            attributes = self.characterCard.attributes
        elif (self.mobCard):
            attributes = self.mobCard.attributes

        self.currentArmor = attributes.armor
        self.currentPower = attributes.power
        self.currentStamina = attributes.stamina

    def getName(self) -> None:
        if (self.characterCard):
            attributes = self.characterCard.name
        elif (self.mobCard):
            attributes = self.mobCard.name
        return attributes

    def getCooldowns(self) -> list[int]:
        cooldowns = []
        
        for skillCard in self.skills.all():
            cooldowns.append(skillCard.remainingCooldown)
        
        return cooldowns

    def getStaminaBase(self) -> float:
        if (self.characterCard):
            attributes = self.characterCard.attributes
        elif (self.mobCard):
            attributes = self.mobCard.attributes

        return attributes.stamina
    
    def getSkillCardUsed(self, skillNumber : int):
        skillCard = self.skills.all().filter(skill__level = skillNumber).first()
        return skillCard
        
    def reduceAllCooldown(self):
        for skillCard in self.skills.all():
            skillCard.reduceCooldown()
            skillCard.reduceEffect()
    
    def applySkill(self, skillNumber : int, target : str) -> None:
        target = Card.objects.all().filter(Q(characterCard__name = target) | Q(mobCard__name = target)).first()
        skillCardUsed = self.getSkillCardUsed(skillNumber)

        skillUsed = skillCardUsed.skill
        if (skillUsed.type == 'Damage'): 
            target.currentStamina -= skillUsed.baseEffect * self.currentPower * (100 - target.currentArmor) * 0.0001
            if (target.currentStamina < 0):
                target.currentStamina = 0
        elif (skillUsed.type == 'Heal'):
            maxStamina = target.getStaminaBase()
            target.currentStamina += skillUsed.baseEffect * self.currentPower * 0.01
            if (target.currentStamina > maxStamina):
                target.currentStamina = maxStamina
        elif (skillUsed.type == 'Power Buff'):
            target.currentPower += skillUsed.baseEffect
            skillCardUsed.updateEffect(target.getName())
        elif (skillUsed.type == 'Armor Buff'):
            target.currentArmor += skillUsed.baseEffect
            skillCardUsed.updateEffect(target.getName())

        target.save()
        skillCardUsed.updateCooldown()

    def skillWithoutCD(self) -> int:
        skillLevels = [3, 2, 1]
        for skillLevel in skillLevels:
            skillCard = self.skills.all().filter(skill__level = skillLevel).first()
            if (skillCard.remainingCooldown == 0):
                return skillLevel

    def getLifeInPercentage(self) -> int:
        percentage = self.currentStamina * 100 / self.getStaminaBase()
        if (percentage > 95):
            return 100
        elif (percentage > 85):
            return 90
        elif (percentage > 75):
            return 80
        elif (percentage > 65):
            return 70
        elif (percentage > 55):
            return 60
        elif (percentage > 45):
            return 50
        elif (percentage > 35):
            return 40
        elif (percentage > 25):
            return 30
        elif (percentage > 15):
            return 20
        elif (percentage > 0):
            return 10
        else:
            return 0