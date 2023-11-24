from .models import Winner

from CharacterSelect.models import characterSelect
from CharacterSelect.views import selectCharacter
from GameSettings.models import GameSetting
from PvESettings.models import PvESetting

# Return a screen to select player characters
def userSelectCharacter(request, faction, player):
    playersCharacter = characterSelect.objects.all()

    if playersCharacter[player].tank == '':
        return selectCharacter(request, faction, 'Tank', player)
    elif playersCharacter[player].melee == '':
        return selectCharacter(request, faction, 'Melee', player)
    elif playersCharacter[player].ranged == '':
        return selectCharacter(request, faction, 'Ranged', player)
    elif playersCharacter[player].heal == '':
        return selectCharacter(request, faction, 'Heal', player)
    else:
        return None
    


# Set parameters from Game Screen.
def setParametersGame() -> dict:
    parameters = {}
    parameters['leftSide'] = getPlayerParameters(0)

    settings = GameSetting.objects.first()
    if (settings.gameMode == 'pve'):
        settingsPvE = PvESetting.objects.first()
        parameters['rightSide'] = getMobParameters(settingsPvE)
        parameters['backgroundPath'] = 'Game/Image/Background/pveBackground'+str(settingsPvE.raid)+'.jpg'
    elif (settings.gameMode == 'pvp'):
        parameters['rightSide'] = getPlayerParameters(1)
        parameters['backgroundPath'] = 'Game/Image/Background/pvpBackground.jpg'

    return parameters

# Set Parameters Result Game.
def setParametersResult() -> dict:
    parameters = {}

    settings = GameSetting.objects.first()
    parameters['mode'] = settings.gameMode

    winner = Winner.objects.first().sideWinner
    if (parameters['mode'] == 'pvp'):
        parameters['result'] = winner + ' wins'

        factionPlayer1 = GameSetting.objects.first().faction
        factionPlayer2 = 'Alliance' if factionPlayer1 == 'Horde' else 'Horde'

        factionWinner = factionPlayer1 if winner == 'Player 1' else factionPlayer2
        parameters['backgroundPath'] = 'Game/Image/Background/' + factionWinner.lower() + 'WinsBackground.png'
    elif (parameters['mode'] == 'pve'):
        if (winner == 'Player 1'):
            raid = PvESetting.objects.first().raid
            parameters['result'] = 'You Win'
            parameters['backgroundPath'] = 'Game/Image/Background/pveBackground'+ raid +'.jpg'
        elif (winner == 'Player 2'):
            parameters['result'] = 'You Lose'
            parameters['backgroundPath'] = 'Game/Image/Background/pveLoseBackground.jpg'

    return parameters

# Format name to remove blank spaces and invalid characters.
def formatName(name : str) -> str:
    nameFormated = name.replace("'", '')
    nameFormated = nameFormated.replace(' ', '')
    return nameFormated

# Return a list with path for images from characters choosen by player.
def getPlayerParameters(player : int) -> list:
    path = 'Game/Image/Cards/'
    characters = characterSelect.objects.all()[player]

    frontCharacters  = [
        {   'name' : characters.tank,
            'path' : path + formatName(characters.tank) + '.png'
        },{
            'name' : characters.melee,
            'path' : path + formatName(characters.melee) + '.png',
        }
    ]
    behindCharacters = [
        {
            'name' : characters.ranged,
            'path' : path + formatName(characters.ranged) + '.png',
        },{
            'name' : characters.heal,
            'path' : path + formatName(characters.heal) + '.png',
        }
    ]

    pathsPlayer = behindCharacters + frontCharacters if player == 0 else frontCharacters + behindCharacters 
    return pathsPlayer

# Return a list with path for images from pve mode.
def getMobParameters(settingsPvE : PvESetting) -> list:
    path = 'Game/Image/Cards/'
    pathsMob = [
        {
            'name' : settingsPvE.easyMob,
            'path' : path + formatName(settingsPvE.easyMob) + '.png',
        },{
            'name' : settingsPvE.mediumMob,
            'path' : path + formatName(settingsPvE.mediumMob) + '.png',
        },{
            'name' : settingsPvE.hardMob,
            'path' : path + formatName(settingsPvE.hardMob) + '.png',
        },{
            'name' : settingsPvE.bossMob,
            'path' : path + formatName(settingsPvE.bossMob) + '.png',
        }
    ]

    return pathsMob

# Create a vector by alternating between the two vectors.
def sortCharacters(characters1 : list[str], characters2: list[str]) -> list[str]:
    characters = []
    countChar1 = 0
    countChar2 = 0
    count = 0
    
    while (count < 8):
        if (count % 2 == 0):
            characters.append(characters1[countChar1])
            countChar1 += 1
        else:
            characters.append(characters2[countChar2])
            countChar2 += 1
        
        count += 1

    return characters