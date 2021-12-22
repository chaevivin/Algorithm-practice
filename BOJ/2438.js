const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

let N = parseInt(input);

for (let i = 1; i <= N; i++) {
  for (let j = 1; j <= i; j++) {
      process.stdout.write('*');
  }
  process.stdout.write('\n');
}
