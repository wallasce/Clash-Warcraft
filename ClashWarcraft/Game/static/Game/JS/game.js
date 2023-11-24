import * as ajax from "./ajax.js";
import * as screenControl from "./screenControl.js"

var round = 0
var skillsNames;
var cardsName;
var skillClicked;

window.onload = (event) => {
    ajax.makeRequestWithPromise('GET', '/api/get-names')
    .then(function (result) {
        cardsName = JSON.parse(result).names;
    })
    .then(ajax.makeRequestWithPromise("GET", "/api/get-skill")
        .then(function(result) {
            skillsNames = JSON.parse(result);
        })
        .then(function() {
            screenControl.updateSkillImageSrc(skillsNames[cardsName[round]])
        })
    )
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

function checkEndGame() {
    player1 = [0, 2, 4, 6]
    player2 = [1, 3, 5, 7]
}

function updateRound() {
    do {
        round = round < 7 ? (round + 1) : 0;
    } while (cardsName[round] == 'Dead');
}

addEventOnClickinCards()
addEventOnClickinSkill()