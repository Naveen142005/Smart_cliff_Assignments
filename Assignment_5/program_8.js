const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

async function main() {
    let s = await cwr.get("Enter a 2D Array: ");
    let arr = s.split(',').map(Number);
    
    arr.sort((a, b) => a - b);
    
    let len = arr.length;

    if (len & 1) 
        console.log(arr[Math.floor(len / 2)] * 1.0);
    else {
        let num1 = arr[len / 2];
        let num2 = arr[(len / 2) - 1];
        console.log((num1 + num2) / 2.0);
    }

    cwr.close();
}

main();
