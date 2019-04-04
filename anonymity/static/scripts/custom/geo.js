(function geo() {

    var elem = document.getElementById('geo');

    navigator.geolocation.watchPosition(

        function (position) {
            elem.innerHTML = 'Im tracking you!';
        },

        function (e) {
            if (e.code == error.PERMISSION_DENIED)
                elem.innerHTML += 'No';
        });
})();
