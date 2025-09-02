const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

async function main() {
    let s = await cwr.get("Enter a date: ");
    let n = await cwr.get("Enter N: ");
    let date = new Date(s);
    // let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    while (n > 0) {
        date.setDate(date.getDate() + 1);   
        let day = date.getDay();           
        if (day !== 0 && day !== 6) {     
            n--; 
        }
    }
    let y = date.toISOString().split("T")[0];
    console.log(y);
    
    
    
    
    cwr.close();
}

main();