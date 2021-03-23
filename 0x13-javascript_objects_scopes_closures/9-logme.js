#!/usr/bin/node
var times = 0;
exports.logMe = function (item) {
    console.log(times + ': ' + item)
    times++;
}
