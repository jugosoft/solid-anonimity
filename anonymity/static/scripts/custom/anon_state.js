var State = function () {
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
        if (tmp.innerText === 'DNS may be leaking.')
            this.dns = true;        

        tmp = document.getElementById('proxies');
        if (tmp.innerText === 'True')
            this.proxies = true;

        tmp = document.getElementById('ports');
        if (tmp.innerText.lenght >= 4)
            this.opened_ports = true;

        //our current state of anonymity level
        this.printState();
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
        if (this.spambases == true)
            console.log('spambases : 1');
    }
}

var state = new State();
state.init();



