#!/usr/bin/node
// this script reads a file parsed and prints

const reader = require('fs');
reader.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
