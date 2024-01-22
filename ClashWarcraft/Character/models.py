from django.db import models
from Skill.models import Skill

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=35, blank=True, default='')
    faction = models.CharField(max_length=8)
    kind = models.CharField(max_length=15)
    type = models.CharField(max_length=6)
    attributes = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)

    def __str__(self) -> str:
        return self.name
    
    def getSkillInformate(self) -> list[tuple]:
        skillName = []
        
        for skill in self.skill.all():
            skillName.append((str(skill), skill.type))
        
        return skillName

class Attribute(models.Model):
    attributesOf = models.CharField(max_length=50, default="")
    armor = models.FloatField()
    power = models.FloatField()
    stamina = models.FloatField()

    def __str__(self) -> str:
        return "Attributes of " + self.attributesOf
    
    def getAttributes(self) -> list[dict]:
        attributeDict = []
        
        attributeDict.append({
            'name' : 'Armor',
            'value' : self.armor,
        })
        attributeDict.append({
            'name' : 'Power',
            'value' : self.power,
        })
        attributeDict.append({
            'name' : 'Stamina',
            'value' : self.stamina,
        })

        return attributeDict