#!/usr/bin/node
const Sqash = require('./5-square');

class Square extends Sqash {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
