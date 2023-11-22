export function updateSkillImageSrc(skillsNames) {
    let skillsBtn = document.getElementsByClassName('skill-btn');
    
    for (let count = 0; count < skillsBtn.length; count += 1) {
        let classType = 'skill-type-'+ skillsNames.type[count].replace(' ', '-').toLowerCase();
        skillsBtn[count].className = 'skill-btn ' + classType;

        let skillImg = skillsBtn[count].getElementsByClassName('skill-img')
        skillImg[0].src = skillsNames.path[count];
        skillImg[0].hidden = false;
        changeCardsDisableValueTo(true)
    }
}

export function changeCardsDisableValueTo(value, sideToChange = 'all') {
    let classCards = (sideToChange == 'all') ? '.card-button' : '.cards-' + sideToChange + ' .card-button';
    let cards = document.querySelectorAll(classCards);

    for (let i = 0; i < cards.length; i+=1) {
        cards[i].disabled = value;
    }
}

export function changeSkillDisableValueTo(value) {
    let div = document.getElementsByClassName('skills');
    let skills = div[0].getElementsByTagName('button');

    for (let i = 0; i < skills.length; i+=1) {
        skills[i].disabled = value;
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