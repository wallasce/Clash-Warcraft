from django.shortcuts import render
from Cards.views import deleteCards
from CharacterSelect.views import resetTeams
from Game.views import resetWinner
from GameSettings.views import resetSettings
from PvESettings.views import resetPve
from WebsiteContent.models import homePagePanel, HeaderPage, SectionPagePanel
from .wrapper import getCharacterParameters, getCharacterDetails

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
    headerPage = HeaderPage.objects.get(page = 'Campaign')
    sectionPagePanels = SectionPagePanel.objects.all().filter(page = 'Campaign')
    context = {
        'campaignsData' : sectionPagePanels,
        'headerPage' : headerPage,
    }

    return render(request, 'WebSite/campaignPage.html', context)

def gamePlayPage(request):
    headerPage = HeaderPage.objects.get(page = 'Game Play')
    sectionPagePanel = SectionPagePanel.objects.all().filter(page = 'Game Play')
    context = {
        'headerPage' : headerPage,
        'sectionPagePanels' : sectionPagePanel,
    }
    return render(request, 'WebSite/gamePlayPage.html', context)