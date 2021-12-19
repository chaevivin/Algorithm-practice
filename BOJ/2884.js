const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

let h = parseInt(input[0]);
let m = parseInt(input[1]);

if (m >= 45) {
  m = m - 45;
  console.log(h + " " + m);
}
else {
  if (h == 0) {
    h = 24;
  }
  h = h - 1;
  m = (m + 60) - 45;
  console.log(h + " " + m);
}
