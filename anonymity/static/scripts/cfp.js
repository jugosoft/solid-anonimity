String.prototype.hashCode = function () {
    var hash = 0, i, chr, len;

    if (this.length == 0)
        return hash;

    for (i = 0, len = this.length; i < len; i++) {
        chr = this.charCodeAt(i);
        hash = ((hash << 5) - hash) + chr;
        hash |= 0;
    }

    return hash;
};

var canvas = document.createElement("canvas");
var context = canvas.getContext("2d");

context.fillText("Do I know you? \ud83d\ude03", 20, 20);

var dataURL = canvas.toDataURL("image/png").substr("data:image/png;base64,".length);
//document.getElementById("cfp").innerHTML = dataURL;
document.getElementById("cfp").innerHTML += "Canvas Fingerprint: " + dataURL.hashCode();
document.body.appendChild(canvas);
//hide IT
canvas.style.display = 'none';