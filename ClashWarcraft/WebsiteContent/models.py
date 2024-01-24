from django.db import models

# Create your models here.
class homePageCard(models.Model):
    title = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=55)
    description = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return 'Card Content ' + str(self.title)
    
    def getData(self) -> dict:
        data = {
            'title' : self.title,
            'subtitle' : self.subtitle,
            'description' : self.description
        }