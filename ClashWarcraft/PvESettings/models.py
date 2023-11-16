from django.db import models

class PvESetting(models.Model):
    raid = models.IntegerField(blank=True, default=0)
    easyMob = models.CharField(max_length=55, blank=True)
    mediumMob = models.CharField(max_length=55, blank=True)
    hardMob = models.CharField(max_length=55, blank=True)
    bossMob = models.CharField(max_length=55, blank=True)