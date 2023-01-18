#!/usr/bin/node
// this script gets the contents of a webpage
// and stores it in a file

const req = require('request');
const fs = require('fs');

req.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', (err2) => {
      if (err2) {
        console.log(err2);
      }
    });
  }
});
