#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

fs.writeFile(argv[2], argv[3], 'utf8', function(err) {
	if (err) {
		console.log(err)
	}
	return
});
