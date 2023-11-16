from django.db import models

# Create your models here.
class characterSelect(models.Model):
    tank = models.CharField(max_length=50, blank=True)
    melee = models.CharField(max_length=50, blank=True)
    ranged = models.CharField(max_length=50, blank=True)
    heal = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return "Character Selected for Player " + str(self.id)