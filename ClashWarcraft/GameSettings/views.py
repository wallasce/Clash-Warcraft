from django.shortcuts import render, HttpResponse

from .models import GameSettings

# Create your views here.
def passInitialScreen(request):
    if (request.method == 'POST'):
        settings = GameSettings.objects.first() 
        settings.passHomeScreen = True
        settings.save()

    return HttpResponse(request)  

def setGameMode(request):
    if (request.method == 'POST'):
        settings = GameSettings.objects.first() 
        settings.gameMode = request.body.decode('utf-8')
        settings.save()

    return HttpResponse(request)

def setFaction(request):
    if (request.method == 'POST'):
        settings = GameSettings.objects.first()
        settings.faction = request.body.decode('utf-8')
        settings.save()

    return HttpResponse(request)
