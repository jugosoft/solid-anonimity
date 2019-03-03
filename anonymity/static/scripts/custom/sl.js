try {
    var plugin = Silverlight.isInstalled(this);

    if (Silverlight.available)
        document.getElementById('sl').innerHTML = "silverlightControlHost";
} catch (e) {
    if (e instanceof ReferenceError) {
        console.log("There is not any kind of SilveLight plugin");
    }
}

 