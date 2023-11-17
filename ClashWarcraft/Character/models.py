from django.db import models
from Skill.models import Skill

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50)
    faction = models.CharField(max_length=8)
    kind = models.CharField(max_length=15)
    type = models.CharField(max_length=6)
    attributes = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)

    def __str__(self) -> str:
        return self.name
    
    def getSkillNames(self) -> list[str]:
        skillName = []
        
        for skill in self.skill.all():
            skillName.append(str(skill))
        
        return skillName

class Attribute(models.Model):
    attributesOf = models.CharField(max_length=50, default="")
    armor = models.FloatField()
    power = models.FloatField()
    stamina = models.FloatField()

    def __str__(self) -> str:
        return "Attributes of " + self.attributesOf