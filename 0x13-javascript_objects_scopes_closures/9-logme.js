#!/usr/bin/node
// Print function with custom characters.

let counter = 0;

exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  counter += 1;
};
