
function payFunction(emp) {
    let { name, salary, role } = emp;
    role = role || "Not Assigned";
    console.log("Employee: " + name + " | Role: " + role + " | Salary: $" + salary);
}

payFunction({ name: "Alice", salary: 60000, role: "Developer" });
payFunction({ name: "Bob", salary: 45000 });
