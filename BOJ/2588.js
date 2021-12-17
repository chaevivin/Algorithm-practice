const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let a = parseInt(input[0]);
let b = parseInt(input[1]);

let val3 = a * (b % 10);
let val4 = a * Math.floor((b % 100) / 10);
let val5 = a * Math.floor(b / 100);
let total = val3 + (val4 * 10) + (val5 * 100);

console.log(val3);
console.log(val4);
console.log(val5);
console.log(total);
