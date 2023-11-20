from django.db import models

from typing import Any
from django.db import models
from Character.models import Character, Attribute

class Card(models.Model):
    characterCard = models.ForeignKey(Character, on_delete=models.CASCADE)
    currentArmor = models.FloatField(blank=True, default=0)
    currentPower = models.FloatField(blank=True, default=0)
    currentStamina = models.FloatField(blank=True, default=0)

    def __str__(self) -> str:
        return 'Card of ' + self.characterCard.name