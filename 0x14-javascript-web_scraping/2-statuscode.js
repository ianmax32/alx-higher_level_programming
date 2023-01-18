#!/usr/bin/node
// this script displays the status code of a get
// request

const request = require('request');
request.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ', response.statusCode);
  }
});
