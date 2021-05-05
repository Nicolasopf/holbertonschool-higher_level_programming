#!/usr/bin/node
const argv = process.argv;
const request = require('request');

request(argv[2], 'utf8', function(error, response, body) {
  if (error) throw(error);
  const tasks_dic = {}
  const result = JSON.parse(body);

  result.forEach(task => {
    if (task.completed == true) {
      if (tasks_dic[task.userId] === undefined) {
		tasks_dic[task.userId] = 1;
	  } else {
		tasks_dic[task.userId]++;
	  }
	}
  });
  console.log(tasks_dic);
});
