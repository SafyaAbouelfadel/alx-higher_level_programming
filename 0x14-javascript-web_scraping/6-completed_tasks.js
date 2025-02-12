#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (!err) {
    const todos = JSON.parse(body);
    const finished = {};
    todos.forEach(todo => {
      if (todo.completed && finished[todo.userId] === undefined) {
        finished[todo.userId] = 1;
      } else if (todo.completed) {
        finished[todo.userId] += 1;
      }
    });
    console.log(finished);
  }
});
