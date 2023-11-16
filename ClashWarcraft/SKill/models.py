from django.db import models

class Skill(models.Model):
    skillOff = models.CharField(max_length=50, blank=True)
    level = models.IntegerField(blank=True)
    type = models.CharField(max_length=25, blank=True)
    cooldown = models.IntegerField(blank=True)
    baseEffect = models.FloatField(blank=True)

    def __str__(self) -> str:
        return self.skillOff + ' ' + str(self.level)