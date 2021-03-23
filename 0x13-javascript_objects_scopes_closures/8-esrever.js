#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  for (let i = list.length - 1; list[i]; i--) {
    arr.push(list[i]);
  }
  return (arr);
};
