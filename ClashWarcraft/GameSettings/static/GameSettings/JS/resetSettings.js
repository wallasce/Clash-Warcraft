if (window.performance.getEntriesByType) {
    if (window.performance.getEntriesByType("navigation")[0].type === "reload") {
        var xhhtp = new XMLHttpRequest();
        xhhtp.open('POST', '/settings/reset', true);
        xhhtp.setRequestHeader('X-CSRFToken', csrftoken); 
        xhhtp.send(true);
    }
}
  
  