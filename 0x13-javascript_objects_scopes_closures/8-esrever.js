#!/usr/bin/node

exports.esrever = function (list) {
  const values = [];
  for (let a = list.length - 1; a >= 0; a--) {
    values.push(list[a]);
  }
  return values;
};
