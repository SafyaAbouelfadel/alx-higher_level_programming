#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, function (err, res, body) {
  if (err) return console.log(err);
  const { characters } = JSON.parse(body);
  characters.forEach((item) => {
    request(item, (err, res, content) => {
      if (err) return console.log(err);
      console.log(JSON.parse(content).name);
    });
  });
});
