#!/usr/bin/node

exports.add = function (x, theFunction) {
  for (let a = 0; a < x; a++) {
    theFunction();
  }
};
