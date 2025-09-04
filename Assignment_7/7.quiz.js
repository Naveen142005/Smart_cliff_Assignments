const { exit } = require("process");
const { consoleRW } = require("./consoleRW");
const crw = new consoleRW();

async function main() {
    //Create a function quizGame() that initializes the score at 0. 
    function quizGame() {
        score = 0
        //Inside it, return an object with two methods: 
        return {
            correct() {
                score += 1;
                console.log(`Score = ${score}`);
            },
            wrong() {
                score -= 1;
                console.log(`Score = ${score}`);
            }

        }
    }
    let n = 5;
    let game = quizGame()
    while (n--) {
        let str = await crw.get('Enter a choice (correct / wrong) : ');
        if (str.toLowerCase() == "correct")
            game.correct()
        else
            game.wrong()
    }
    // Ensure the score variable cannot be directly accessed or modified outside the function. 
    console.log(game.score);
    
    crw.close();
}

main();