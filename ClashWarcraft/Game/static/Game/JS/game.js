import * as ajax from "./ajax.js";
import * as screenControl from "./screenControl.js"

var round = 0
var skillsNames;
var cardsName;
var skillClicked;
var gameMode;

window.onload = async function() {
    let response = await ajax.makeRequest('GET', '/api/get-names'); 
    cardsName = JSON.parse(response).names;

    response = await ajax.makeRequest('GET', '/api/get-skill'); 
    skillsNames = JSON.parse(response);

    response = await ajax.makeRequest('GET', '/api/get-game-mode');
    gameMode = JSON.parse(response).mode;
    console.log(gameMode)

    screenControl.updateSkillImageSrc(skillsNames[cardsName[round]])
}

function addEventOnClickinSkill() {
    let skillsBtn = document.getElementsByClassName('skill-btn');

    for (let i = 0; i < skillsBtn.length; i+=1) {
        skillsBtn[i].onclick = function() {
            skillClicked = this.value;
            screenControl.changeSkillDisableValueTo(true)

            let skillType = this.className.split(' ')[1]
            screenControl.enablesCardsToRound(round, skillType)
        };
    }
}

async function addEventOnClickinCards() {
    let cards = document.getElementsByClassName('card-button');

    for (let i = 0; i < cards.length; i+=1) {
        cards[i].onclick = async function() {
            let parameters = JSON.stringify({
                'currentCard' : cardsName[round],
                'skillNumber' : skillClicked,
                'targetCard' : this.value,
            });
            await ajax.makeRequest('POST', '/api/apply-skill', parameters);
            screenControl.updateBar(this.value);
            let isDead = await screenControl.changeCardToDead(this);
            if (isDead) {
                setCardNameToDeath(this.value);
                await checkEndGame()
            }

            screenControl.changeCardsDisableValueTo(true);
            screenControl.changeSkillDisableValueTo(false);

            updateRound()
            screenControl.updateSkillImageSrc(skillsNames[cardsName[round]])
        };
    }
}

function setCardNameToDeath(name) {
    let index = cardsName.indexOf(name);
    cardsName[index] = 'Dead';
}

async function checkEndGame() {
    let sides = ['left', 'right'];
    for (let count = 0; count < sides.length; count++) {
        let sidDiv = document.querySelectorAll('.cards-' + sides[count] + ' .card-dead');
        if (sidDiv.length == 4) {
            await ajax.makeRequest('POST', '/settings/set-winner', sides[count]);
            window.location.href = ''
        }
    }
}

function updateRound() {
    do {
        round = round < 7 ? (round + 1) : 0;
    } while (cardsName[round] == 'Dead');
}

addEventOnClickinCards()
addEventOnClickinSkill()