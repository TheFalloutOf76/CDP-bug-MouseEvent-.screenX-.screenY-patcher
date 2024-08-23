Object.defineProperty(MouseEvent.prototype, 'screenX', {
    get: function () {
        return this.clientX + window.screenX;
    }
});

Object.defineProperty(MouseEvent.prototype, 'screenY', {
    get: function () {
        return this.clientY + window.screenY;
    }
});
