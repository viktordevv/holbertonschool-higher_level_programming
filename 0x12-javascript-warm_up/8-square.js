#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size) {
  for (let q = 0; q < size; ++q) {
    let p = 0;

    for (; p < size; ++p) {
      process.stdout.write('X');
    }

    if (p === size) {
      console.log('');
    }
  }
} else {
  console.log('Missing size');
}
