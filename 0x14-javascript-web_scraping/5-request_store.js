#!/usr/bin/node
const argv = process.argv
const request = require('request')
const fs = require('fs')

request(argv[2], 'utf8', function(err, response) {
	if (err) {
		console.log(err)
		return
	}
	fs.writeFile(argv[3], response.body, 'utf-8', function(err) {
		if (err) {
			console.log(err)
		}
		return
	})
})
