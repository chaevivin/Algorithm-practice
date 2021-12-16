const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

let a = parseInt(input[0]);
let b = parseInt(input[1]);

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(Math.floor(a / b));  // 정수 출력을 위해 소수점 이하 버림
console.log(a % b);
