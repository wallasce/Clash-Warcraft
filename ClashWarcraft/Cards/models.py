from django.db import models

from django.db import models
from Character.models import Character

class Card(models.Model):
    characterCard = models.ForeignKey(Character, on_delete=models.CASCADE)
    currentArmor = models.FloatField(blank=True, default=0)
    currentPower = models.FloatField(blank=True, default=0)
    currentStamina = models.FloatField(blank=True, default=0)

    def __str__(self) -> str:
        return 'Card of ' + self.characterCard.name
    
    def applySkill(self, skillNumber : int, target : str) -> None:
        target = Card.objects.all().filter(characterCard__name = target).first()
        skillUsed = self.characterCard.skill.all().filter(level = skillNumber).first()

        if (skillUsed.type == 'Damage'):
            target.currentStamina -= skillUsed.baseEffect * self.currentPower * (100 - target.currentArmor) * 0.0001
            target.save()