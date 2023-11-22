export var names;

var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value

export function makeRequestWithPromise(method, url) {
    return new Promise(function (resolve) {
        var xhttp = new XMLHttpRequest();
        xhttp.open(method, url, true);
        xhttp.onload = function () {
          if (this.status == 200) {
            resolve(xhttp.response);
          } 
        };
        xhttp.send();
    });
}

export function makePostRequest(url, value) {
  var xhttp = new XMLHttpRequest();
  xhttp.open('POST', url, true);
  xhttp.setRequestHeader("X-CSRFToken", csrftoken); 
  xhttp.send(value);
}