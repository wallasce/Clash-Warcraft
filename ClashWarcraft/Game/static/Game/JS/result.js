import * as ajax from "./ajax.js";

var buttons = document.getElementsByTagName('button');

for (let i = 0; i < buttons.length; i++) {
    let button = buttons[i];
    button.onclick = async function() {
        if (this.value == 'exit'){
            window.location.href = '/'
        } else {
            await ajax.makeRequest('POST', '/settings/end-game', this.value)
            window.location.href = ''
        }
    }
}