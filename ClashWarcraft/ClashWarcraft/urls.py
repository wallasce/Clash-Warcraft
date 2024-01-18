"""
URL configuration for ClashWarcraft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Cards.views import applySkill, getCooldowns, isDead, reduceCooldown
from CharacterSelect.views import setCharacter
from Game.views import game, getCharacterName, getPercentage, setWinner, resultRequest, getGameMode
from GameSettings.views import passInitialScreen, resetSettings, setFaction, setGameMode, passLoadScreen
from Skill.views import getSkillFromCharacterSelected
from Website.views import homePage, characterPage, characterDetails, campaignPage, gamePlayPage

urlpatterns = [
    path("", homePage, name = 'HomePage'),
    path("admin/", admin.site.urls),
    path("campaign/", campaignPage, name = 'Campaign'),
    path("character/", characterPage, name = 'Character'),
    path("character/<characterName>", characterDetails, name = 'Character'),
    path("game/", game, name = 'Game'),
    path("game-play/", gamePlayPage, name = 'GamePlay'),
    path("api/apply-skill", applySkill, name = 'ApplySkill'),
    path("api/get-cooldown/", getCooldowns, name = 'GetCooldown'),
    path("api/get-names", getCharacterName, name = 'GetName'),
    path("api/get-game-mode", getGameMode, name = 'GetGameMode'),
    path("api/get-skill", getSkillFromCharacterSelected, name = 'GetSkill'),
    path("api/get-percentage/", getPercentage, name = 'GetPercentage'),
    path("api/is-dead/", isDead, name = 'IsDead'),
    path("api/reduce-cooldown", reduceCooldown, name = 'ReduceCooldown'),
    path("settings/end-game", resultRequest, name = 'ResultRequest'),
    path("settings/faction", setFaction, name = 'SetFaction'),
    path("settings/game-mode", setGameMode, name = 'SetGameMode'),
    path("settings/pass-initial-screen", passInitialScreen, name = 'passInitialScreen'),
    path("settings/load-screen", passLoadScreen, name = 'passLoadScreen'),
    path("settings/reset", resetSettings, name = 'ResetSettings'),
    path("settings/setCharacter", setCharacter, name = 'Set Character'),
    path("settings/set-winner", setWinner, name = 'SetWinner'),
]
