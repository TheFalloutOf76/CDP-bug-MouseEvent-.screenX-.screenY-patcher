let patchScript = `
Object.defineProperty(MouseEvent.prototype, 'screenX', {
    value: 1234,
    writable: false
})

Object.defineProperty(MouseEvent.prototype, 'screenY', {
    value: 567,
    writable: false
})
`;

let element = document.createElement('script');
element.innerHTML = patchScript;
document.documentElement.appendChild(element);