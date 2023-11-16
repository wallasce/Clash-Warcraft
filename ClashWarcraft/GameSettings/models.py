from django.db import models

# Create your models here.
class GameSetting(models.Model):
    passHomeScreen = models.BooleanField(blank=True, default=False)
    gameMode = models.CharField(max_length=3, blank=True)
    faction = models.CharField(max_length=8, blank=True)

    def __str__(self) -> str:
        return "Game Settings"