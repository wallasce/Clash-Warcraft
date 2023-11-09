from django.db import models

# Create your models here.
class GameSettings(models.Model):
    passHomeScreen = models.BooleanField(blank=True, default=False)
    gameMode = models.CharField(max_length=3, blank=True)
    faction = models.CharField(max_length=8, blank=True)