#!/usr/bin/node
// Print function with custom characters.

exports.converter = function (base) {
  function conver (num) {
    return num.toString(base);
  }
  return conver;
};
