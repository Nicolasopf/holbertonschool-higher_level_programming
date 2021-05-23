#!/usr/bin/node
const fs = require('fs');
const av = process.argv;
const first = fs.readFileSync(av[2], 'UTF-8');
const second = fs.readFileSync(av[3], 'UTF-8');
fs.writeFileSync(av[4], (first + second), 'UTF-8');
