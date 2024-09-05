"use strict";
// keyof
function print(obj) {
    let key;
    for (key in obj) {
        // ✅
        console.log(key, obj[key].toUpperCase());
    }
}
// Object.keys()
function print(obj) {
    Object.keys(obj).forEach((k) => {
        // ✅
        console.log(k, obj[k].toUpperCase());
    });
}
