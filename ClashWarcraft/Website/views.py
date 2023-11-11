from django.shortcuts import render
from CharacterSelect.views import resetTeams
from GameSettings.views import resetSettings

# Create your views here.
def homePage(request):
    resetSettings()
    resetTeams()
    return render(request, 'WebSite/homePage.html')