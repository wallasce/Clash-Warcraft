import * as ajax from "./ajax.js";
import * as effect from "./effect.js"

function removeClassSkillType(skillBtn) {
    let classTypes = ['damage', 'heal', 'armor-buff', 'power-buff'];
    for (let count = 0; count < classTypes.length; count++) {
        skillBtn.classList.remove('skill-type-' + classTypes[count]);
    }
}

export function updateSkillImageSrc(skillsNames) {
    let skillsBtn = document.getElementsByClassName('skill-btn');
    
    for (let count = 0; count < skillsBtn.length; count += 1) {
        let classType = 'skill-type-'+ skillsNames.type[count].replace(' ', '-').toLowerCase();
        removeClassSkillType(skillsBtn[count]);
        skillsBtn[count].classList.add(classType);

        let skillImg = skillsBtn[count].getElementsByClassName('skill-img')
        skillImg[0].src = skillsNames.path[count];
        skillImg[0].hidden = false;
        changeCardsDisableValueTo(true)
    }
}

// This functions disable all elements in screen to computer play.
export function disablePlayerControl() {
    let skillsBtn = document.getElementsByClassName('skill-btn');
    
    for (let count = 0; count < skillsBtn.length; count += 1) {
        let skillImg = skillsBtn[count].getElementsByClassName('skill-img')
        skillImg[0].hidden = true;
        changeCardsDisableValueTo(true)
    }
}

export function changeCardsDisableValueTo(value, sideToChange = 'all') {
    let classCards = (sideToChange == 'all') ? '.card-button' : '.cards-' + sideToChange + ' .card-button';
    let cards = document.querySelectorAll(classCards);

    for (let i = 0; i < cards.length; i+=1) {
        if(cards[i].className.includes('card-dead')){
            cards[i].disabled = true;
            effect.changeHoverPropertyOnCard(cards[i], true);
        }else{
            cards[i].disabled = value;
            effect.changeHoverPropertyOnCard(cards[i], value);
        }
    }
}

export function changeSkillDisableValueTo(value) {
    let div = document.getElementsByClassName('skills');
    let skills = div[0].getElementsByTagName('button');

    for (let i = 0; i < skills.length; i+=1) {
        skills[i].disabled = value;
        effect.changeHoverPropertyOnSkill(skills[i], value);
    }
}

export function updateBar(from) {
    var xhttp = new XMLHttpRequest();
    xhttp.open('GET', '/api/get-percentage?from='+from, true);
    xhttp.onreadystatechange = function() {
        if (this.status == 200 && this.readyState == 4) {
            let bar = document.getElementsByClassName('bar-' + from)[0];
            let responseDict = JSON.parse(this.response);
            bar.src = '/static/Game/Image/Bars/'+ responseDict.percentage + '.png';
        }
    }
    xhttp.send();
}

export async function changeCardToDead(card) {
    let response = await ajax.makeRequest('GET', '/api/is-dead?character=' + card.value);
    let responseDict = JSON.parse(response);
    if (responseDict.isDead) {
        card.classList.add('card-dead');
        
        let cardImg = card.firstElementChild;
        cardImg.src = '/static/Game/Image/Cards/Dead.png';
        
        return true
    }
    return false
}

function enableRight() {
    changeCardsDisableValueTo(true, 'left');
    changeCardsDisableValueTo(false, 'right');
}

function enableLeft() {
    changeCardsDisableValueTo(false, 'left');
    changeCardsDisableValueTo(true, 'right');
}

export function enablesCardsToRound(round, typeSkill) {
    if (round % 2 == 0) {
        if (typeSkill == 'skill-type-damage') {
            enableRight()
        } else {
            enableLeft()
        }
    } else {
        if (typeSkill == 'skill-type-damage') {
            enableLeft()
        } else {
            enableRight()
        }
    }
}