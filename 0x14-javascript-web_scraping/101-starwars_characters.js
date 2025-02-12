#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, function (err, res, body) {
  if (err) return console.log(err);
  const { characters } = JSON.parse(body);
  printCharacters(characters, 0);
});

function printCharacters (character, index) {
  request(character[index], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < character.length) printCharacters(character, index + 1);
    }
  });
}
