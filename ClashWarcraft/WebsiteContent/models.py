from django.db import models

from ImageManager.models import UploadedImage
class homePagePanel(models.Model):
    title = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=55)
    description = models.CharField(max_length=1000)
    image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return 'Panel: ' + str(self.title)
    
    def getData(self) -> dict:
        data = {
            'title' : self.title,
            'subtitle' : self.subtitle,
            'description' : self.description
        }

        return data