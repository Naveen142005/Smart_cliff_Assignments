const { exit } = require("process");
const { consoleRW } = require("./consoleRW");
const crw = new consoleRW();

async function main() {
    let employees = [
        { name: "A", salary: 60000 },
        { name: "B", salary: 40000 },
        { name: "C", salary: 25000 },
        { name: "D", salary: 50000 },
        { name: "E", salary: 30000 }
    ];
    let arr = []
    employees.forEach(item => arr.push(item.salary))
    console.log("High earners", employees.filter(item => item.salary > 50000));
    console.log("Medium earners", employees.filter(item => item.salary <= 50000 && item.salary >= 30000));
    console.log("Low earnres", employees.filter(item => item.salary < 30000));
    // console.log(`Medium Earners`, employees.forEach(item => item.salary != max(arr)));



    crw.close();
}

main();