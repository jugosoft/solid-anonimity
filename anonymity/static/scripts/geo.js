(function geo() {

    var elem = document.getElementById('geo');
    elem.innerHTML = "Does someone track your location? ";

    navigator.geolocation.watchPosition(

        function (position) {
            elem.innerHTML += " I'm tracking you!";
        },

        function (e) {
            if (e.code == error.PERMISSION_DENIED)
                elem.innerHTML += "No";
        });
})();
