const { consoleRW } = require("./consoleRW");
const crw = new consoleRW();



async function main() {
    let students = [
        { name: "Alice", marks: 80 },
        { name: "Bob", marks: 60 },
        { name: "larwin", marks: 80 },
        { name: "larwin kumar", marks: 60 },
        { name: "prabu", marks: 80 }
    ];

    console.log("Students list....");
    console.log(students);


    const sortStudents = (students, comparator) => students.sort(comparator)
    

    let str = await crw.get("Sort by : (name or marks): ")
    
    if (str == "name") 
        sortStudents(students, (a, b) => (a.name).localeCompare(b.name))
    else if (str == "marks")
         sortStudents(students, (b, a) => a.marks - b.marks)
    else 
        console.log("Invalid selection.");

    console.log(students);
           
    crw.close();
}

main();