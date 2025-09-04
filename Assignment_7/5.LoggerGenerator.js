const { exit } = require("process");
const { consoleRW } = require("./consoleRW");
const crw = new consoleRW();

async function main() {
    let str = await crw.get("Enter a log:");
    
    const ErrorLogger = () => "[ERROR] Something went wrong! "
    const InfoLogger  = () => "[INFO] System is running fine. "

    const createLogger = (level) => {
        level = level.toLowerCase();
        if (level == "error") 
                return ErrorLogger
        else if (level == "info")
                return InfoLogger
        else
            return () => "Invalid Log"
    }

    const log = createLogger(str);
    console.log(log());
    
    
    crw.close();
}

main();