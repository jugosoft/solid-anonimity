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

    // Detect WMP Version
    if ($.getVersion) {
        P.version = $.getVersion(P.name, instantiate);
        out.innerHTML += ("Plugin version: " + P.version);
    }


    // Detect Plugin Status
    if ($.isMinVersion) {
        P.status = $.isMinVersion(P.name, P.minVersion, instantiate);
        out.innerHTML += "Plugin status: " + getStatusMsg(P);
        out.innerHTML += "";
    }


    var INFO = $.getInfo ? $.getInfo(P.name, instantiate) : null;

    if (INFO) {
        out.innerHTML += "Plugin is scriptable: " + (INFO.Scriptable ? "true" : "false");

        if (INFO.DllPlugin && !INFO.FirefoxPlugin) {
            out.innerHTML += "";
            out.innerHTML += "Note: It appears you are using the old Windows Media Player plugin (Dynamic Link Library).";
            out.innerHTML += "We recommend that you upgrade to the Windows Media Player Firefox plugin.";
        }

        if (INFO.DllPlugin && INFO.FirefoxPlugin) {
            out.innerHTML += "";
            out.innerHTML += "Note: you appear to have BOTH the old Windows Media Player plugin (Dynamic Link Library) " +
                "AND the new Windows Media Player Firefox plugin. You can disable the old plugin " +
                "in your browser to avoid any potential conflict between the two.";
        }

        if (P.status === 0 && INFO.FirefoxPlugin) {
            out.innerHTML += "";
            out.innerHTML += "Note: if you want the plugin version to be detected, then you will need to use the " +
                "'instantiate' input argument.";
            out.innerHTML += "You may also have to give your browser security permission to run the plugin.";
        }
    }
    
    if ($.browser.isIE) {
        out.innerHTML += "";

        out.innerHTML += "ActiveX enabled / ActiveX scripting enabled: " +
            $.browser.ActiveXEnabled ? "true" : "false [this may prevent the plugin from running in Internet Explorer]";

        out.innerHTML += "ActiveX Filtering enabled: " +
            $.browser.ActiveXFilteringEnabled ? "true [this may prevent the plugin from running in Internet Explorer]" : "false";
    }

})(); 
