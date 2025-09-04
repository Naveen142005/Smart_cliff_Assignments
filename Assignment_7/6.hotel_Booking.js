const { exit } = require("process");
const { consoleRW } = require("./consoleRW");
const crw = new consoleRW();

async function main() {
    console.log("Types of rooms...");
    console.log(`Standard (default choice)\nDeluxe (premium option)`);
    
    function bookRoom(type = "Standard", nights = 1) {
        console.log(`Room booked: ${type} for ${nights}(s)`);
    }
    
    let str = await crw.get("You may Enter a type:");
    let night = await crw.get("You may Enter a nights:");
    
    bookRoom();

     str = await crw.get("You must Enter a type:");
     night = await crw.get("You must Enter a nights:");

    bookRoom(str , night);

    crw.close();
}

main();