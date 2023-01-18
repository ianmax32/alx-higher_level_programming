#!/usr/bin/node
// this script writes a string to a file

const writer = require('fs');
writer.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) {
    console.log(err);
  }
});
