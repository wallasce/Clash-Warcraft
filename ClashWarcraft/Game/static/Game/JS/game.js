import * as ajax from "./ajax.js";
import * as screenControl from "./screenControl.js"

var round = 0
window.onload = (event) => {
    var names;
    var skills;

    ajax.makeRequest('GET', '/api/get-names')
    .then(function (result) {
        names = JSON.parse(result).names;
    })
    .then(ajax.makeRequest("GET", "/api/get-skill")
        .then(function(result) {
            skills = JSON.parse(result);
        })
        .then(function() {
            let skillsImg = document.getElementsByClassName('skill');
            for (let count = 0; count < skillsImg.length; count += 1) {
                skillsImg[count].src = skills[names[round]][count];
                skillsImg[count].hidden = false;
            }
        })
    )
}