#!/usr/bin/node

const SquareMain = require('./5-square');

class Square extends SquareMain {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let a = 0; a < this.height; a++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
