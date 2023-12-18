export function activeSkill(skill) {
    skill.classList.add('active');
}

export function deactiveSkill() {
    let skill = document.querySelector('.skill-btn.active');
    skill.classList.remove('active');
}