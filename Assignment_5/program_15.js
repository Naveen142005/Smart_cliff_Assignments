const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

async function main() {
    let s = await cwr.get("Enter text: ");
    if (typeof s !== "string") {
        console.log([]);
    } else {
        const matches = s.match(/\d+(\.\d+)?/g);
        console.log(matches ? matches.map(Number) : []);
    }
    cwr.close();
}

main();
