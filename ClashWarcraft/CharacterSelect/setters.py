from .models import characterSelect
from django.db.models.manager import BaseManager

def setTank(name : str, teams : BaseManager[characterSelect]) -> None:
    for team in teams:
        if team.tank == '':
            team.tank = name
            team.save()