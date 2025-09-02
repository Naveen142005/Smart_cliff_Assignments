const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

async function main() {
    let s = await cwr.get("Enter a Number: ");
    let digit = s.length
    let sum = 0

    for (let i = 0; i < s.length; i += 1) {
        sum += (Number(s.charAt(i))) ** digit;
    }
    console.log(sum == s)
    cwr.close();
}

main();
