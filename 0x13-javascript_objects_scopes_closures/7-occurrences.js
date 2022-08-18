#!/usr/bin/node
// Returns the number of occurrences.

exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
