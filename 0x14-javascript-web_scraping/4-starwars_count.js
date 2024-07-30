#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body);
    const info2 = info.results;

    for (let i = 0; i < info2.length; i++) {
      if (info2[i].characters) {
        for (const j of info2[i].characters) {
          if (j.includes('18')) {
            count++;
          }
        }
      }
    }
    console.log(count);
  }
});
