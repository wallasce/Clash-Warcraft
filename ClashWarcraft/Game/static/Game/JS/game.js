import * as ajax from "./ajax.js";
import * as screenControl from "./screenControl.js"

var round = 0
window.onload = (event) => {
    var names;
    var skills;

    ajax.makeRequest('GET', '/api/get-names')
    .then(function (result) {
        names = JSON.parse(result).names;
    })
    .then(ajax.makeRequest("GET", "/api/get-skill")
        .then(function(result) {
            skills = JSON.parse(result);
        })
        .then(function() {
            let skillsImg = document.getElementsByClassName('skill');
            for (let count = 0; count < skillsImg.length; count += 1) {
                skillsImg[count].src = skills[names[round]][count];
                skillsImg[count].hidden = false;
                screenControl.changeCardsDisableValueTo(true)
            }
        })
    )
}

function addEventOnClickinSkill(){
    let div = document.getElementsByClassName('skills');
    let skills = div[0].getElementsByTagName('button');

    for (let i = 0; i < skills.length; i+=1) {
        skills[i].onclick = function() {
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
            screenControl.changeCardsDisableValueTo(true);
            screenControl.changeSkillDisableValueTo(false);

            round = round < 8 ? (round + 1) : 0
        };
    }
}

addEventOnClickinCards()
addEventOnClickinSkill()