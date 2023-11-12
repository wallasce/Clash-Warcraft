from django.db import models

class Mob(models.Model):
    name = models.CharField(max_length=50)
    raid = models.CharField(max_length=8)
    level = models.CharField(max_length=15)
    attributes = models.ForeignKey("Attributes", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Attributes(models.Model):
    attributesOf = models.CharField(max_length=50, default="")
    armor = models.FloatField()
    power = models.FloatField()
    stamina = models.FloatField()

    def __str__(self) -> str:
        return "Attributes of " + self.attributesOf