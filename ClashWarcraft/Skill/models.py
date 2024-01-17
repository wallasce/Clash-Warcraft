from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)
    skillOff = models.CharField(max_length=50, blank=True)
    level = models.IntegerField(blank=True)
    type = models.CharField(max_length=25, blank=True)
    cooldown = models.IntegerField(blank=True)
    baseEffect = models.FloatField(blank=True)
    durationEffect = models.IntegerField(blank=True, default=0)

    def __str__(self) -> str:
        return self.skillOff + ' ' + str(self.level)