const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

let N = Number(input);
let answer = '';

for (let i = N; i >= 1; i--) {
  answer += i + '\n';
}

console.log(answer);
