var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

function passLoadScreen() {
    var xhhtp = new XMLHttpRequest();
    xhhtp.open('POST', '/settings/load-screen', true);
    xhhtp.onreadystatechange = function () {
        window.location.href = '';
    }
    xhhtp.setRequestHeader('X-CSRFToken', csrftoken); 
    xhhtp.send(true);
}

setTimeout(passLoadScreen, 5000);