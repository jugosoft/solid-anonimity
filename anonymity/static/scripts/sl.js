Silverlight.isInstalled(this);
var silverlight = document.getElementById('sl');

if (Silverlight.available) {
    silverlight.innerHTML = "noSilverlight";
} else {
    silverlight.innerHTML = "silverlightControlHost";
}
 