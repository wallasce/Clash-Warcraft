from django.db import models

# Create your models here.
class Winner(models.Model):
    sideWinner = models.CharField(max_length=10, blank=True)

    def __str__(self) -> str:
        return "Game Winner"