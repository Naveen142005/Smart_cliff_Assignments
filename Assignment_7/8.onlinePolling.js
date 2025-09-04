const { exit } = require("process");
const { consoleRW } = require("./consoleRW");
const crw = new consoleRW();

async function main() {

    const countVotes = (candidate, ...votes) => 
         `${candidate} received ${votes.filter(person => person === candidate).length} votes`;
    
    console.log(countVotes("Alice", "Bob", "Alice", "Eve", "Alice", "Bob"));
    console.log(countVotes("Bob", "Bob", "Alice", "Eve", "Alice", "Bob"));
    console.log(countVotes("Eve", "Bob", "Alice", "Eve", "Alice", "Bob"));
    crw.close();
}

main();