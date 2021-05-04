#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (error, code, body) {
  if (error) throw code;
  console.log('code:', code && code.statusCode);
});
