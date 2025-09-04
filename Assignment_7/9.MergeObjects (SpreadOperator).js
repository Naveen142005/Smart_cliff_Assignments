const { exit } = require("process");
const { consoleRW } = require("./consoleRW");
const crw = new consoleRW();

async function main() {
    let personalInfo = { name: "Alice", age: 25 };
    let jobInfo = { role: "Developer", salary: 60000 };

    let mergedInfo = { ...personalInfo, ...jobInfo };

    console.log(mergedInfo);
    crw.close();
}

main();