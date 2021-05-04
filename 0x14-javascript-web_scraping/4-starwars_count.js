#!/usr/bin/node
const argv = process.argv;
const request = require('request');

request(argv[2], function(err, response, body) {
	if (err) {
		console.log(err);
		return;
	}
	text = JSON.parse(body);
	var count = 0;
	for (const i of text.results) {
		if ((String(i.characters).search("people/18")) > 0) {
			count++;
		}
	}
	console.log(count);
})
