#!/usr/bin/node
const argv = process.argv;
const request = require('request')

request(argv[2], function(err, response) {
	if (err) {
		console.log(err)
	}
	else {
		console.log("code: " + response.statusCode)
	}
	return
})
