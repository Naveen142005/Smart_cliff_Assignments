const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

async function main() {
    let s = await cwr.get("Enter password: ");
    if (typeof s !== "string") {
        console.log(false);
    } else {
        const pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$/;
        console.log(pattern.test(s));
    }
    cwr.close();
}

main();
