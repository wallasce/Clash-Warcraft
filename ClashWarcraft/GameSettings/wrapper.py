from PvESettings.models import PvESetting

def getLocalToTravel(gameMode : str) -> str:
    locals = {
        'pvp' : 'Azeroth',
        1 : 'Pandaria',
        2 : 'Black Temple',
        3 : 'Icecrown Citadel',
        4 : 'Dragon Soul',
    }

    key = ''

    if (gameMode == 'pvp'):
        key = gameMode
    else:
        settingsPvE = PvESetting.objects.first()
        key = settingsPvE.raid

    return locals[key]

    