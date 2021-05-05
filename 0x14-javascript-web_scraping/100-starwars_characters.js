#!/usr/bin/node
const argv = process.argv;
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + argv[2], 'utf8', function (error, response, body) {
  if (error) throw (error);
  const result = JSON.parse(body);
  const chars = result.characters;
  chars.forEach(person => {
    request(person, 'utf8', function (error, response, body) {
      if (error) throw error;
      console.log(JSON.parse(body).name);
    });
  });
});
