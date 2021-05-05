#!/usr/bin/node
const argv = process.argv;
const request = require('request');

request(argv[2], 'utf8', function (error, response, body) {
  if (error) throw (error);
  const tasksDic = {};
  const result = JSON.parse(body);

  result.forEach(task => {
    if (task.completed === true) {
      if (tasksDic[task.userId] === undefined) {
        tasksDic[task.userId] = 1;
      } else {
        tasksDic[task.userId]++;
      }
    }
  });
  console.log(tasksDic);
});
