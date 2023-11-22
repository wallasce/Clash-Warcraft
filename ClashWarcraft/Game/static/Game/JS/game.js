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

function addEventOnClickinCards() {
    let cards = document.getElementsByClassName('card-button');

    for (let i = 0; i < cards.length; i+=1) {
        cards[i].onclick = function() {
            let parameters = JSON.stringify({
                'currentCard' : cardsName[round],
                'skillNumber' : skillClicked,
                'targetCard' : this.value,
            });
            ajax.makePostRequest('/api/apply-skill', parameters);
            screenControl.updateBar(this.value)

            screenControl.changeCardsDisableValueTo(true);
            screenControl.changeSkillDisableValueTo(false);

            round = round < 7 ? (round + 1) : 0
            screenControl.updateSkillImageSrc(skillsNames[cardsName[round]])
        };
    }
}

addEventOnClickinCards()
addEventOnClickinSkill()