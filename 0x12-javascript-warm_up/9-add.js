#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const args = process.argv;
const num = add(parseInt(args[2]), parseInt(args[3]));
console.log(num);
