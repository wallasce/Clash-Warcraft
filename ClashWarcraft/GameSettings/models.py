from django.db import models

# Create your models here.
class GameSettings(models.Model):
    passHomeScreen = models.BooleanField()
    gameMode = models.CharField(max_length=3)
    faction = models.CharField(max_length=8)