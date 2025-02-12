#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (!err) {
    const { results } = JSON.parse(body);
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((char) => char.endsWith('/18/')) ? count + 1 : count;
    }, 0));
  }
});
