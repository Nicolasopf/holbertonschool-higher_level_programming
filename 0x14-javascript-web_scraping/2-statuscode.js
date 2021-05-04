#!/usr/bin/node
const argv = process.argv;
const request = require('request');

request(argv[2], function (error, code, body) {
  if (error) throw code;
  console.log("code: " + code.statusCode);
});
