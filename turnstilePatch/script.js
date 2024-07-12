let patchScript = `
let oldAddEventListener = HTMLElement.prototype.addEventListener;

HTMLElement.prototype.addEventListener = addEventListener = function(type, callback) {
    function interceptor(event) {
        event.__defineGetter__('screenX',()=>1234)
        event.__defineGetter__('screenY',()=>567)
        console.log(event, event.screenX, event.screenY);
        callback.call(this, event);
    }
    if (type == 'click') {
        return oldAddEventListener.call(this, type, interceptor);
    }
    return oldAddEventListener.call(this, type, callback);
}`;

let element = document.createElement('script');
element.innerHTML = patchScript;
document.documentElement.appendChild(element);