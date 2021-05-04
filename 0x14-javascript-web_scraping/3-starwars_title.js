#!/usr/bin/node
const argv = process.argv;
const request = require('request')

request("https://swapi-api.hbtn.io/api/films/" + argv[2], function(err, response) {
	if (err) {
		console.log(err)
	}
	else {
		console.log(response.body.split("\"")[3])
	}
})
