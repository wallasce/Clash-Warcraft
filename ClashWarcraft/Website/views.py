from django.shortcuts import render
from Cards.views import deleteCards
from CharacterSelect.views import resetTeams
from Game.views import resetWinner
from GameSettings.views import resetSettings
from PvESettings.views import resetPve

# Create your views here.
def homePage(request):
    resetSettings()
    resetTeams()
    resetPve()
    deleteCards()
    resetWinner()
    return render(request, 'WebSite/homePage.html')