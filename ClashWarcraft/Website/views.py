from django.shortcuts import render
from Cards.views import deleteCards
from CharacterSelect.views import resetTeams
from Game.views import resetWinner
from GameSettings.views import resetSettings
from PvESettings.views import resetPve
from .wrapper import getCharacterParameters, getCharacterDetails, getLoreData, getTutorial

# Create your views here.
def homePage(request):
    resetSettings()
    resetTeams()
    resetPve()
    deleteCards()
    resetWinner()
    return render(request, 'WebSite/homePage.html')

def characterPage(request):
    pathImageFaction = 'GameSettings/Image/FactionSelect/'
    
    hordeParameters = getCharacterParameters('Horde')
    allianceParameters = getCharacterParameters('Alliance')
    parameters = {
        'factions' : [
            {
                'value' : 'Horde',
                'path' : pathImageFaction + 'horde.png'
            },{
                'value' : 'Alliance',
                'path' : pathImageFaction + 'alliance.png'
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