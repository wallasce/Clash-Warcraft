from django.shortcuts import render
from GameSettings.views import resetSettings

# Create your views here.
def homePage(request):
    resetSettings()
    return render(request, 'WebSite/homePage.html')