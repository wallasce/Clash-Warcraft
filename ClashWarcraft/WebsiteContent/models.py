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
        return 'Button on ' + self.page + ': ' + self.text
    
class HeaderPage(models.Model):
    title = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=55)
    description = models.CharField(max_length=155, blank=True, null=True)
    imageContent = models.ForeignKey(UploadedImage, on_delete=models.CASCADE, blank=True, null=True, related_name='ImageUploaded2ContentImage')
    background = models.ForeignKey(UploadedImage, on_delete=models.CASCADE, blank=True, null=True)
    buttons = models.ManyToManyField(button, blank=True)
    page = models.CharField(max_length = 55, blank=True, null=True)
    style = models.CharField(max_length = 55, blank=True, null=True)

    def __str__(self) -> str:
        return 'Header Page: ' + self.title

class SectionPagePanel(models.Model):
    title = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=55)
    description = models.CharField(max_length=1000)
    preSectionPanel = models.ForeignKey(UploadedImage, blank=True, null=True, on_delete=models.CASCADE, related_name='ImageUploaded2preSectionPanel')
    imagesSectionPage = models.ManyToManyField(UploadedImage, blank=True)
    backgroundSectionPage = models.ForeignKey(UploadedImage, on_delete=models.CASCADE, related_name='ImageUploaded2BackgroundSection')
    page = models.CharField(max_length = 55)
    style = models.CharField(max_length = 100, blank=True, null=True)

    def __str__(self) -> str:
        return 'Section Page: ' + self.title