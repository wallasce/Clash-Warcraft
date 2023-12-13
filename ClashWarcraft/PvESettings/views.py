from django.shortcuts import render
from .models import PvESetting
from Mob.models import Mob

def resetPve():
    settings = PvESetting.objects.first()

    settings.raid = 1
    settings.easyMob = ''
    settings.mediumMob = ''
    settings.hardMob = ''
    settings.bossMob = ''

    settings.save()

def setMobs():
    settings = PvESetting.objects.first()
    raid = settings.raid

    mobsRaid = Mob.objects.all().filter(raid = raid)
    settings.easyMob = mobsRaid.filter(level = 'Easy')[0].name
    settings.mediumMob = mobsRaid.filter(level = 'Medium')[0].name
    settings.hardMob = mobsRaid.filter(level = 'Hard')[0].name
    settings.bossMob = mobsRaid.filter(level = 'Boss')[0].name

    settings.save()