#!/usr/bin/node
// this script prints the title of the star wars
// movies where the episode number matches the
// given integer

const request = require('request');
const apiurl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(apiurl, (err, response, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(data).title);
  }
});
