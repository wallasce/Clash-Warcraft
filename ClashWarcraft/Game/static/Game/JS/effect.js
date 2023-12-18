function addActive(element) {
    element.classList.add('active');
}

function removeActive(element) {
    element.classList.remove('active');
}

export function activeSkill(skill) {
    skill.classList.add('active');
}

export function deactiveSkill() {
    let skill = document.querySelector('.skill-btn.active');
    skill.classList.remove('active');
}

export function initiateTurn(cardName) {
    let card = document.querySelector('button[value="'+cardName+'"]');
    addActive(card);
}

export function endTurn() {
    let card = document.querySelector('.card-button.active');
    removeActive(card)
}