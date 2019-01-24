function detectAB() {
    if (window.showAds) {
        // Your user is not using adblocker
        document.getElementById('228').innerHTML += 'No Adblocker detected.'
    } else {
        // You user uses adbocker, show a popup dialog, alert, etc here
        document.getElementById('228').innerHTML += 'You have Adblocker!'
    }
}

function startDetecting() {
    detectAB();
}

startDetecting();