#!/usr/bin/node
let times = 0;
exports.logMe = function (item) {
  console.log(times + ': ' + item);
  times++;
};
