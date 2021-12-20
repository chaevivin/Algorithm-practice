const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let T = Number(input[0]);
let total = '';

for (let i = 1; i <= T; i++) {
    let num = input[i].split(' ');
    total += Number(num[0]) + Number(num[1]) + '\n';
}

console.log(total);
