from django.db import models
from Skill.models import Skill

class Mob(models.Model):
    name = models.CharField(max_length=50)
    raid = models.CharField(max_length=8)
    level = models.CharField(max_length=15)
    attributes = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)

    def __str__(self) -> str:
        return self.name

class Attribute(models.Model):
    attributesOf = models.CharField(max_length=50, default="")
    armor = models.FloatField()
    power = models.FloatField()
    stamina = models.FloatField()

    def __str__(self) -> str:
        return "Attributes of " + self.attributesOf