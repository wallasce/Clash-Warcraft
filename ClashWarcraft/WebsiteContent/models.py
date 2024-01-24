from django.db import models

from ImageManager.models import UploadedImage
class homePagePanel(models.Model):
    title = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=55)
    description = models.CharField(max_length=1000)
    imageManager = models.ForeignKey(UploadedImage, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return 'Panel: ' + str(self.title)