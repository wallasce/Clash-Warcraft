from django.db import models

def directory_path(instance, filename):
    return 'ImageManager/uploads/{0}/{1}'.format(instance.location, filename)

class UploadedImage(models.Model):
    name = models.CharField(max_length=55)
    location = models.CharField(max_length = 100)
    image = models.ImageField(upload_to=directory_path, blank=True)

    def __str__(self) -> str:
        return "Image " + self.name