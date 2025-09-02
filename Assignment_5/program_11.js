const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

async function main() {
    let s = await cwr.get("Enter a 2D Array: ");
    const date = new Date(s);
    let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    console.log(days[date.getDay()]);
    
    cwr.close();
}

main();