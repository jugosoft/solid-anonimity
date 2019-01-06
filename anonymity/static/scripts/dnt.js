function dnt() {
    var dntEnabled = navigator.doNotTrack || 1 === (navigator.doNotTrack || window.doNotTrack || navigator.msDoNotTrack) ? true : false;
    var element = document.getElementById('dnt');
    element.innerHTML = 'Do Not Track is enabled = ' + dntEnabled;
}

dnt();

