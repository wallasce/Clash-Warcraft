import * as ajax from "./ajax.js";
import * as effect from "./effect.js"
import * as screenControl from "./screenControl.js"
import * as pve from "./pve.js"

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

    if (gameMode == 'pve') {
        pve.initializeThreats(cardsName);
    }

    screenControl.updateSkillImageSrc(skillsNames[cardsName[round]]);
    effect.initiateTurn(cardsName[round]);
    screenControl.changeSkillDisableValueTo(false);
}

async function applySkill(cardClicked, parameters) {
    await ajax.makeRequest('POST', '/api/apply-skill', parameters);
    screenControl.updateBar(cardClicked.value);
    let isDead = await screenControl.changeCardToDead(cardClicked);
    if (isDead) {
        setCardNameToDeath(cardClicked.value);
        await checkEndGame();
    }
}

function addEventOnClickinSkill() {
    let skillsBtn = document.getElementsByClassName('skill-btn');

    for (let i = 0; i < skillsBtn.length; i+=1) {
        skillsBtn[i].onclick = function() {
            effect.activeSkill(this);

            skillClicked = this.value;
            screenControl.changeSkillDisableValueTo(true);

            let skillType = this.className.split(' ')[1];
            screenControl.enablesCardsToRound(round, skillType);
        };
    }
}

async function addEventOnClickinCards() {
    let cards = document.getElementsByClassName('card-button');

    for (let i = 0; i < cards.length; i+=1) {
        cards[i].onclick = async function() {
            effect.deactiveSkill();
            let parameters = JSON.stringify({
                'currentCard' : cardsName[round],
                'skillNumber' : skillClicked,
                'targetCard' : this.value,
            });
            await applySkill(this, parameters);

            screenControl.changeCardsDisableValueTo(true);
            screenControl.changeSkillDisableValueTo(false);

            await updateRound();
            screenControl.updateSkillImageSrc(skillsNames[cardsName[round]]);
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
            window.location.href = '';
        }
    }
}

function checkCompurterTurn(round) {
    let roundMob = [1,3,5,7];
    return (gameMode == 'pve' && roundMob.includes(round));
}

function wait(time) {
    return new Promise(resolve => {
        setTimeout(resolve, time);
    });
}

async function updateRound() {
    effect.endTurn();
    do {
        round = round < 7 ? (round + 1) : 0;
        // Computer play.
        if (checkCompurterTurn(round) && cardsName[round] != 'Dead') {
            effect.initiateTurn(cardsName[round]);
            screenControl.disablePlayerControl();
            await wait(4000)
            pve.computerPlay();
            effect.endTurn();
        } 
    } while (cardsName[round] == 'Dead' || checkCompurterTurn(round));
    effect.initiateTurn(cardsName[round]);
}

addEventOnClickinCards();
addEventOnClickinSkill();