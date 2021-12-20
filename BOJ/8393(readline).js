const readline = require('readline');

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r1.on('line', function (line) {
    input.push(line);
}).on('close', function () {
    let n = Number(input[0]);
    let total = 0;
    
    for (let i = 1; i <= n; i++) {
      total = total + i;
    }
    
    console.log(total);
    
    process.exit();
});
