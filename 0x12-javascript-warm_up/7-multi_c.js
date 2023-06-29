#!/usr/bin/node

let i = parseInt(process.argv[2]);
if (isNaN(i)) {
  console.log('Missing number of occurrence');
} else {
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
