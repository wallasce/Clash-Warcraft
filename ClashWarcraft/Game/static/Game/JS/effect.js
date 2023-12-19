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

export function addClassToHoverOnSkill(skills) {
    for (let count = 0; count < skills.length; count += 1) {
        skills[count].classList.add('clickable')
    }
}

export function removeClassToHoverOnSkill(skills) {
    for (let count = 0; count < skills.length; count += 1) {
        skills[count].classList.remove('clickable')
    }
}