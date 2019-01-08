(function webglDetect() {

    DEBUG = 1;

    const gl_implementations = [
        "webgl2", "experimental-webgl2",
        "webgl", "experimental-webgl",
        "moz-webgl", "fake-webgl"
    ];

    var supported_implementations = [],
        ctx = false,
        impl_ctx = ctx;

    for (var index in gl_implementations) {
        impl_ctx = false;
        try {
            impl_ctx = document.createElement("canvas").getContext(gl_implementations[index], {stencil: true});

            if (impl_ctx){
                if (ctx) {
                    //destroyWebgl(impl_ctx);
                }
                else {
                    ctx = impl_ctx;
                }
                supported_implementations.push(gl_implementations[index]);
            }
        }
        catch (e) {
            if (DEBUG) {
                console.warn("webglDetect", e);
            }
        }
    }

    console.log(ctx + " " + supported_implementations);

    var elem = document.getElementById('webgl');
    elem.innerHTML = 'possible :-( ';
}) ();