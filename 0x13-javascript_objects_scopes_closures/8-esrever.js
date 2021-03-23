#!/usr/bin/node
exports.esrever = function (list) {
    let arr = [];
    for (i = list.length - 1; list[i]; i--) {
	arr.push(list[i]);
    }
    return (arr);
}
