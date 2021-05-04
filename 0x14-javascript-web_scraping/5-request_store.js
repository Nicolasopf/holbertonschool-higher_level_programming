#!/usr/bin/node
const argv = process.argv
const request = require('request')
const fs = require('fs')

request(argv[2], 'utf8', function(error, response) {
  if (error) {
    return console.error(error);
  }
  fs.writeFile(argv[3], response.body, 'utf-8', function(error) {
	if (error) {
   	  return console.error(error)
	}
  });
});
