#!/usr/bin/node
const request = require('request');
const argv = process.argv;
let count = 0;

request(argv[2], function (error, response) {
  if (error) {
    return console.error(error);
  }
  const jsonResp = JSON.parse(response.body);
  for (const film of jsonResp.results) {
    for (const actor of film.characters) {
      if (actor.split('/')[5] === '18') {
        count += 1;
      }
    }
  }
  console.log(count);
});
