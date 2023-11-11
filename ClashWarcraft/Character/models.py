from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50)
    faction = models.CharField(max_length=8)
    kind = models.CharField(max_length=15)
    type = models.CharField(max_length=6)
    attributes = models.ForeignKey("Attributes", on_delete=models.CASCADE)
    path = models.ForeignKey("Path", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Attributes(models.Model):
    attributesOf = models.CharField(max_length=50, default="")
    armor = models.FloatField()
    power = models.FloatField()
    stamina = models.FloatField()

    def __str__(self) -> str:
        return "Attributes of " + self.attributesOf

class Path(models.Model):
    pathOf = models.CharField(max_length=50, default="")
    imageSelection = models.CharField(max_length=50)
    imageGame = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return "Path of " + self.pathOf