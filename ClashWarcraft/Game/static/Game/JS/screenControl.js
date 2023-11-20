export function changeCardsDisableValueTo(value, sideToChange) {
    let side = document.getElementsByClassName('cards-' + sideToChange);
    let cards = side[0].getElementsByTagName('button');

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