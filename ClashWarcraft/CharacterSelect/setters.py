from .models import characterSelect
from django.db.models.manager import BaseManager

def setTank(name : str, teams : BaseManager[characterSelect]) -> None:
    for team in teams:
        if team.tank == '':
            team.tank = name
            team.save()

def setMelee(name : str, teams : BaseManager[characterSelect]) -> None:
    for team in teams:
        if team.melee == '':
            team.melee = name
            team.save()

def setRanged(name : str, teams : BaseManager[characterSelect]) -> None:
    for team in teams:
        if team.ranged == '':
            team.ranged = name
            team.save()

def setHeal(name : str, teams : BaseManager[characterSelect]) -> None:
    for team in teams:
        if team.heal == '':
            team.heal = name
            team.save()