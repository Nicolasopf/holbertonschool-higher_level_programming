#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (error, response) {
  if (error) {
    return console.error(error);
  }
  const jsonResp = JSON.parse(response.body);
  console.log(jsonResp.title);
});
