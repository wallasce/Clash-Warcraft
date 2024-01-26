from django.db import models

from ImageManager.models import UploadedImage
class homePagePanel(models.Model):
    title = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=55)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length = 55, blank=True, null=True)
    imageManager = models.ForeignKey(UploadedImage, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return 'Panel: ' + str(self.title)

class button(models.Model):
    text = models.CharField(max_length=55)
    link = models.CharField(max_length=55)
    background = models.ForeignKey(UploadedImage, on_delete=models.CASCADE, blank=True, null=True)
    page = models.CharField(max_length=55, blank = True, null=True)
    style = models.CharField(max_length=55)

    def __str__(self) -> str:
        return 'Button ' + self.style + ' on ' + self.page + ': ' + self.text