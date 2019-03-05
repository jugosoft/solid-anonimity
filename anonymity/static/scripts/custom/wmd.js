/*
 * This script is going to check and find 
 * Windows Media Plugin
 * We have to protect ourselves from this
 * find of evil
*/

// detects the plugin
(function () {

    // Return text message based on plugin detection result
    var getStatusMsg = function (obj) {

        if (obj.status === 1)
            return "installed & enabled, version is >= " + obj.minVersion;

        if (obj.status === 0)
            return "installed & enabled, version is unknown";

        if (obj.status === -0.1)
            return "installed & enabled, version is < " + obj.minVersion;

        if (obj.status === -0.2)
            return "installed but not enabled";

        if (obj.status === -1)
            return "not installed or not enabled";

        if (obj.status === -3)
            return "error...bad input argument to PluginDetect method";

        return "unknown";
    };  

    // for output
    var out = document.getElementById('wmd');
   
    // Object that holds all data on the plugin
    var P = {
        name: "WindowsMediaPlayer",
        mime: "",
        status: -1,
        version: null,
        minVersion: "11,0,0,0"
    };

    var $ = PluginDetect,

    // The 'instantiate' input argument only affects non-Internet Explorer browsers.       
    // For Internet Explorer, the plugin version will always be detected regardless
    // of the value of 'instantiate'.
        instantiate = false;

    if ($.getVersion(P.name, instantiate) !== null) {

        // Detect WMP Version
        if ($.getVersion) {
            P.version = $.getVersion(P.name, instantiate);
            out.innerHTML += " Plugin version: " + P.version;
        }


        // Detect Plugin Status
        if ($.isMinVersion) {
            P.status = $.isMinVersion(P.name, P.minVersion, instantiate);
            out.innerHTML += " Plugin status: " + getStatusMsg(P);
            out.innerHTML += "";
        }
    } else {
        out.innerHTML += " status: is not detected";
    }

    if ($.browser.isIE) {
        out.innerHTML += "";

        out.innerHTML += "ActiveX enabled / ActiveX scripting enabled: " +
            $.browser.ActiveXEnabled ? "true" : "false [this may prevent the plugin from running in Internet Explorer]";

        out.innerHTML += "ActiveX Filtering enabled: " +
            $.browser.ActiveXFilteringEnabled ? "true [this may prevent the plugin from running in Internet Explorer]" : "false";
    }

})(); 
