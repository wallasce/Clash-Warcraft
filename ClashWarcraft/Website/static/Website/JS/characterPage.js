function getOpositeFaction(faction) {
    if (faction == 'Horde') {
        return 'Alliance'
    } else {
        return 'Horde'
    }
}

function selectFactionToShow(faction) {
    let opositeFaction = getOpositeFaction(faction)

    // Change Faction Select.
    let buttonSelect = document.getElementsByClassName('button-'+faction)[0];
    buttonSelect.classList.add('selected');

    let buttonDisable = document.getElementsByClassName('button-'+opositeFaction)[0];
    buttonDisable.classList.remove('selected');

    // Change Characters showed.
    let divToShow = document.getElementsByClassName('container-'+ faction +'-list')[0];
    divToShow.hidden = false;

    let divToHidden = document.getElementsByClassName('container-'+ opositeFaction +'-list')[0];
    divToHidden.hidden = true;
}

function initialize(){
    selectFactionToShow('Horde');

    let buttons = document.getElementsByClassName('button-faction');

    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', function(){
            selectFactionToShow(this.value);
        })
    }
}

initialize()