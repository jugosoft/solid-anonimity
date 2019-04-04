var State = function () {
    //number for displaying on
    //gauge chart
    this.level = 100;

    this.dns = null;
    this.proxies = null;
    this.opened_ports = null;
    this.js = null;
    this.tor = null;
    this.flash = null;
    this.webrtc = null;
    this.location = null;
    this.silverlight = null;
    this.loggedin = null;
    this.winmediaplayer = null;
    this.spambases = null;

    this.init = function () {
        var tmp = document.getElementById('dns2');
        if (tmp.innerText === 'DNS may be leaking.') {
            this.dns = true;
            this.level -= 8;
        }

        tmp = document.getElementById('proxies');
        if (tmp.innerText === 'True') {
            this.proxies = true;
            this.level -= 8;
        }

        tmp = document.getElementById('ports');
        if (tmp.innerText.lenght >= 4) {
            this.opened_ports = true;
            this.level -= 8;
        }

        tmp = document.getElementById('js');
        if (tmp.innerHTML == 'JS is really working! Stop it!') {
            this.js = true;
            this.level -= 8;
        }

        tmp = document.getElementById('tor');
        if (tmp.innerHTML == 'True') {
            this.tor = true;
            this.level -= 8;
        }

        tmp = document.getElementById('fp');
        if (tmp.innerHTML == 'Flash Player is enabled') {
            this.flash = true;
            this.level -= 8;
        }

        tmp = document.getElementById('rtc');
        if (tmp.innerHTML.length > 29) {
            this.webrtc = true;
            this.level -= 8;
        }

        tmp = document.getElementById('geo');
        if (tmp.innerHTML == 'Im tracking you!') {
            this.location = true;
            this.level -= 8;
        }
        tmp = document.getElementById('sl');
        if (tmp.innerHTML != 'impossible...') {
            this.silverlight = true;
            this.level -= 8;
        }

        tmp = document.getElementById('loggedIn');
        if (tmp.childElementCount > 0) {
            this.loggedin = true;
            this.level -= 8;
        }

        tmp = document.getElementById('wmd');
        if (!tmp.innerHTML.includes('is not detected')) {
            this.winmediaplayer = true;
            this.level -= 8;
        }

        //our current state of anonymity level
        this.printState();

        //update meter's data
        config.data.current = this.level;

    }

    this.printState = function () {
        if (this.dns == true)
            console.log('dns : 1');
        if (this.proxies == true)
            console.log('proxies : 1');
        if (this.opened_ports == true)
            console.log('opened_ports : 1');
        if (this.js == true)
            console.log('js : 1');
        if (this.tor == true)
            console.log('tor : 1');
        if (this.flash == true)
            console.log('flash : 1');
        if (this.webrtc == true)
            console.log('webrtc : 1');
        if (this.location == true)
            console.log('location : 1');
        if (this.silverlight == true)
            console.log('silverlight : 1');
        if (this.loggedin == true)
            console.log('loggedin : 1');
        if (this.winmediaplayer == true)
            console.log('winmediaplayer : 1');

        console.log('current level is ' + this.level);
    }
}

var state = new State();
state.init();
