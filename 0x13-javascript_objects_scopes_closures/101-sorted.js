#!/usr/bin/node
const dic = require('./101-data').dict;
const new_dict = {};
for (const key in dic) {
  new_dict[dic[key]] = [];
}
for (const key in dic) {
  new_dict[dic[key]].push(key);
}
console.log(new_dict)
