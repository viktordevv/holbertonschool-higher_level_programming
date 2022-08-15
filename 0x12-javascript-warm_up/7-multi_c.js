#!/usr/bin/node

const limites = parseInt(process.argv[2]);
if (limites) {
  for (let i = 0; i < limites; ++i) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
