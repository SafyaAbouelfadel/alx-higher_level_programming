#!/usr/bin/node
const request = require('request');
request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  function (err, response, body) {
    console.log(err || JSON.parse(body).title);
  }
);
