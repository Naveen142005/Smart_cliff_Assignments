let customet_details = [
    { id: "101", name: "Naveen", items: [{ name: "Watch", price: 2000 }, { name: "Bag", price: 1000 }], status: "Delivered" },
    { id: "102", name: "Kumar", items: [{ name: "Shoes", price: 1500 }, { name: "Belt", price: 500 }], status: "Pending" },
    { id: "103", name: "Larwin", items: [{ name: "Laptop", price: 50000 }, { name: "Mouse", price: 1500 }], status: "Delivered" },
    { id: "104", name: "Prabha", items: [{ name: "Mobile", price: 30000 }, { name: "Charger", price: 1000 }], status: "Pending" }
];

//map
console.log("Customer Names");
console.log(customet_details.map(item => item.name));
console.log('\n\n');


//reduce
console.log("Customer Items");
let totalCost = 0;
customet_details.forEach(order => {
    let orderTotal = order.items.reduce((sum, item) => sum + item.price, 0);
    totalCost += orderTotal;
});
console.log("Total Cost:", totalCost);
console.log('\n\n')


//forEach;
console.log("All Customer Details");
customet_details.forEach(item => {
    console.log(item);

})
console.log('\n\n');

//filter
console.log("Delivered Orders");
customet_details.filter(item => item.status === "Delivered").forEach(item => {
    console.log(item);

})