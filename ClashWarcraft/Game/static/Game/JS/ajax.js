export var names;

var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value

export function makeRequest(method, url, parameters = null) {
  return new Promise(function (resolve, reject) {
      let xhttp = new XMLHttpRequest();
      xhttp.open(method, url);
      xhttp.onload = function () {
          if (this.status >= 200 && this.status < 300) {
              resolve(xhttp.response);
          } else {
              reject({
                  status: this.status,
                  statusText: xhttp.statusText
              });
          }
      };
      xhttp.onerror = function () {
          reject({
              status: this.status,
              statusText: xhttp.statusText
          });
      };
      if (parameters) {
        xhttp.setRequestHeader("X-CSRFToken", csrftoken); 
        xhttp.send(parameters);
      } else {
        xhttp.send();
      }
  });
}

export function makePostRequest(url, value) {
  var xhttp = new XMLHttpRequest();
  xhttp.open('POST', url, true);
  xhttp.setRequestHeader("X-CSRFToken", csrftoken); 
  xhttp.send(value);
}