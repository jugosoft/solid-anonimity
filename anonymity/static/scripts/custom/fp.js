function a(self) {

    var xFlash, plugins = navigator.plugins, shockwave = navigator.mimeTypes &&
        navigator.mimeTypes['application/x-shockwave-flash'];

  xFlash = function() {
    var versions, result;

      result = false;

    versions = [
      'ShockwaveFlash.ShockwaveFlash.6',
      'ShockwaveFlash.ShockwaveFlash.7',
      'ShockwaveFlash.ShockwaveFlash'
    ];

    for(var i = 0; i < versions.length; i++) {
        if (!result)
            try {
                result = new ActiveXObject(versions[i]);
            } catch (e) {
                console.log(e);
            }
    }

    return !!result;
  };

  self.hasFlashPlayer = plugins && plugins.length && shockwave && shockwave.enabledPlugin ||
    (typeof ActiveXObject !== 'undefined' && xFlash()) || false;

} (window) ? document.getElementById('fp').innerHTML = 'Flash Player is enabled' :
    document.getElementById('fp').innerHTML = 'Flash Player is disabled';