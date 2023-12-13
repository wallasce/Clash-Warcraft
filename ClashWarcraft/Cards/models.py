from django.db import models

from django.db import models
from Character.models import Character
from Mob.models import Mob

class Card(models.Model):
    characterCard = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)
    mobCard = models.ForeignKey(Mob, on_delete=models.CASCADE, null=True)
    currentArmor = models.FloatField(blank=True, default=0)
    currentPower = models.FloatField(blank=True, default=0)
    currentStamina = models.FloatField(blank=True, default=0)

    def __str__(self) -> str:
        return 'Card of ' + self.characterCard.name
    
    def initialize(self) -> None:
        if (self.characterCard):
            attributes = self.characterCard.attributes
        elif (self.mobCard):
            attributes = self.mobCard.attributes

        self.currentArmor = attributes.armor
        self.currentPower = attributes.power
        self.currentStamina = attributes.stamina
    
    def applySkill(self, skillNumber : int, target : str) -> None:
        target = Card.objects.all().filter(characterCard__name = target).first()
        skillUsed = self.characterCard.skill.all().filter(level = skillNumber).first()

        if (skillUsed.type == 'Damage'): 
            target.currentStamina -= skillUsed.baseEffect * self.currentPower * (100 - target.currentArmor) * 0.0001
            if (target.currentStamina < 0):
                target.currentStamina = 0

            target.save()
        elif (skillUsed.type == 'Heal'):
            maxStamina = target.characterCard.attributes.stamina
            target.currentStamina += skillUsed.baseEffect * self.currentPower * 0.01
            if (target.currentStamina > maxStamina):
                target.currentStamina = maxStamina

            target.save()

    def getLifeInPercentage(self) -> int:
        percentage = self.currentStamina * 100 / self.characterCard.attributes.stamina
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