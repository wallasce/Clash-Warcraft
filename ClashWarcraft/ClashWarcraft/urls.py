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

from CharacterSelect.views import setCharacter
from Game.views import game, getCharacterName
from GameSettings.views import passInitialScreen, resetSettings, setFaction, setGameMode
from Skill.views import getSkillFromCharacterSelected
from Website.views import homePage

urlpatterns = [
    path("", homePage, name = 'HomePage'),
    path("admin/", admin.site.urls),
    path("game/", game, name = 'Game'),
    path("api/get-names", getCharacterName, name = 'GetName'),
    path("api/get-skill", getSkillFromCharacterSelected, name = 'GetSkill'),
    path("settings/faction", setFaction, name = 'SetFaction'),
    path("settings/game-mode", setGameMode, name = 'SetGameMode'),
    path("settings/pass-initial-screen", passInitialScreen, name = 'passInitialScreen'),
    path("settings/reset", resetSettings, name = 'ResetSettings'),
    path("settings/setCharacter", setCharacter, name = 'Set Character'),
]
