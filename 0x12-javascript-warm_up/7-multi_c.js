#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);
if (num === num) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
