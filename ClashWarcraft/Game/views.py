from django.shortcuts import render

# Create your views here.
def game(request):
    pathImageModeSelect = 'Game/Image/ModeSelect/'

    parameters = {
        'types' : [
            {
                'value' : 'pvp',
                'path' : pathImageModeSelect + 'pvp.png',
            },{
                'value' : 'pve',
                'path' : pathImageModeSelect + 'pve.png',
            },
        ]        
    }
    return render(request, 'Game/modeSelect.html', parameters)