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
            updateSkillImageSrc()
        })
    )
}

function updateSkillImageSrc() {
    let skillsImg = document.getElementsByClassName('skill');
    
    for (let count = 0; count < skillsImg.length; count += 1) {
        skillsImg[count].src = skillsNames[cardsName[round]][count];
        skillsImg[count].hidden = false;
        screenControl.changeCardsDisableValueTo(true)
    }
}

function addEventOnClickinSkill() {
    let div = document.getElementsByClassName('skills');
    let skills = div[0].getElementsByTagName('button');

    for (let i = 0; i < skills.length; i+=1) {
        skills[i].onclick = function() {
            skillClicked = this.value;
            screenControl.changeSkillDisableValueTo(true)

            if (round % 2 == 0) {
                screenControl.changeCardsDisableValueTo(true, 'left');
                screenControl.changeCardsDisableValueTo(false, 'right');
            } else {
                screenControl.changeCardsDisableValueTo(false, 'left');
                screenControl.changeCardsDisableValueTo(true, 'right');
            }
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

            screenControl.changeCardsDisableValueTo(true);
            screenControl.changeSkillDisableValueTo(false);

            round = round < 7 ? (round + 1) : 0
            updateSkillImageSrc()
        };
    }
}

addEventOnClickinCards()
addEventOnClickinSkill()