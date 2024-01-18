from django.db import models

# Create your models here.
class Winner(models.Model):
    sideWinner = models.CharField(max_length=10, blank=True)

    def __str__(self) -> str:
        return "Game Winner"
    
class Lore(models.Model):
    title = models.CharField(max_length=35)
    subtitle = models.CharField(max_length=75)
    heading = models.CharField(max_length=45)
    subheading = models.CharField(max_length=65)
    description = models.CharField(max_length=1000)
    raid = models.IntegerField()

    def __str__(self) -> str:
        return self.title
    
class Tutorial(models.Model):
    step = models.IntegerField()
    title = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=55)
    description = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return 'Tutorial - Step ' + str(self.step)
