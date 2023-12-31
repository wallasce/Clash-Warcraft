function addActive(element) {
    element.classList.add('active');
}

function removeActive(element) {
    element.classList.remove('active');
}

export function activeSkill(skill) {
    addActive(skill);
}

export function deactiveSkill() {
    let skill = document.querySelector('.skill-btn.active');
    removeActive(skill);
}

export function initiateTurn(cardName) {
    let card = document.querySelector('button[value="'+cardName+'"]');
    addActive(card);
}

export function endTurn() {
    let card = document.querySelector('.card-button.active');
    removeActive(card)
}

export function changeHoverPropertyOnSkill(skill, disable) {
    if (disable) {
        skill.classList.remove('clickable');
    } else {
        skill.classList.add('clickable');
    }
}

export function changeHoverPropertyOnCard(card, disable) {
    if (disable) {
        card.classList.remove('clickable');
    } else {
        card.classList.add('clickable');
    }
}