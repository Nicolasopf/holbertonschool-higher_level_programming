#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
