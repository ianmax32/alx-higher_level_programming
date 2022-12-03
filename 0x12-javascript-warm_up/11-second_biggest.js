#!/usr/bin/node

const values = [];
if (arguments.length === 1) {
  console.log('0');
} else {
  values.append(Array.prototype.slice(arguments).sort().reverse());
  console.log(values[1]);
}
