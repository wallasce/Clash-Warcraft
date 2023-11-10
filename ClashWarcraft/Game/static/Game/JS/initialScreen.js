var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value

window.addEventListener('keydown', function(event){
    var xhhtp = new XMLHttpRequest();
    xhhtp.open('POST', '/settings/pass-initial-screen', true);
    xhhtp.setRequestHeader('X-CSRFToken', csrftoken); 
    xhhtp.send(true);
})