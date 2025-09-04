const { exit } = require("process");
const { consoleRW } = require("./consoleRW");
const crw = new consoleRW();



async function main() {
    let str = await crw.get("Enter a season:");

    str = str.toLowerCase()
    //base case
    if (str != "summer" && str  != "winter") {
        console.log("Invaild choice...");
        exit();
    }
    const summer  = () => 10
    const winter  = () => 20
    const getDiscountFunction = (season) => {
        if (season == "summer") 
            return  summer;
        return  winter
            
    }
    console.log(`You will be received ${getDiscountFunction(str)()}% discount`);
          
    crw.close();
}

main();