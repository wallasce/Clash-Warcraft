from django.shortcuts import render
from Cards.views import deleteCards
from CharacterSelect.views import resetTeams
from Game.views import resetWinner
from GameSettings.views import resetSettings
from PvESettings.views import resetPve
from WebsiteContent.models import homePagePanel, HeaderPage
from .wrapper import getCharacterParameters, getCharacterDetails, getLoreData, getTutorial

# Create your views here.
def homePage(request):
    resetSettings()
    resetTeams()
    resetPve()
    deleteCards()
    resetWinner()

    homePagePanels = homePagePanel.objects.all()
    headerPage = HeaderPage.objects.get(page = 'HomePage')
    context = {
        'headerPage' : headerPage,
        'panelsContent' : homePagePanels,
    }

    return render(request, 'WebSite/homePage.html', context)

def characterPage(request):
    pathImageFaction = 'GameSettings/Image/FactionSelect/'
    
    hordeParameters = getCharacterParameters('Horde')
    allianceParameters = getCharacterParameters('Alliance')
    parameters = {
        'factions' : [
            {
                'value' : 'Alliance',
                'path' : pathImageFaction + 'alliance.png'
            },{
                'value' : 'Horde',
                'path' : pathImageFaction + 'horde.png'
            }
        ],
        'hordeCharacters' : hordeParameters,
        'allianceCharacters' : allianceParameters,
    }

    return render(request, 'WebSite/characterPage.html', parameters)

def characterDetails(request, characterName):
    charaterParameters = getCharacterDetails(characterName)

    return render(request, 'WebSite/characterDetailsPage.html', charaterParameters)

def campaignPage(request):
    paramtersPage = getLoreData()
    return render(request, 'WebSite/campaignPage.html', paramtersPage)

def gamePlayPage(request):
    parametersPage = getTutorial()
    return render(request, 'WebSite/gamePlayPage.html', parametersPage)