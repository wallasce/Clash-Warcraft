from django.shortcuts import render
from CharacterSelect.views import resetTeams
from GameSettings.views import resetSettings
from PvESettings.views import resetPve

# Create your views here.
def homePage(request):
    resetSettings()
    resetTeams()
    resetPve()
    return render(request, 'WebSite/homePage.html')