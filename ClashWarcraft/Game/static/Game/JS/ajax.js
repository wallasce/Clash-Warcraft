export var names;

export function makeRequest(method, url) {
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