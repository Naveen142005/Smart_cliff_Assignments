const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();
const bigInt = require("big-integer");

async function main() {
    let a = (await cwr.get("Enter String_1: "));
    let b = (await cwr.get("Enter String_2: "));
    a = bigInt(a)
    b = bigInt(b)
    console.log(a.add(b).toString()); 
    cwr.close();
}

main();
