var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value

var buttons = document.getElementsByTagName('button');

for (let i = 0; i < buttons.length; i++) {
    let button = buttons[i];
    
    button.onclick = function() {
        var xhhtp = new XMLHttpRequest();
        xhhtp.open('POST', '/settings/faction', true);
        xhhtp.onreadystatechange = function () {
            window.location.href = ''
        }
        xhhtp.setRequestHeader('X-CSRFToken', csrftoken); 
        xhhtp.send(button.value);
    }
}