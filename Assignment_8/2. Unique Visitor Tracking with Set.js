const user = new Set();

function addUser(userId) {
    user.add(userId);
}

addUser("Naveen_136")
addUser("Larwin_151")
addUser("Prabha_178")
addUser("Naveen_136")

console.log(user)
console.log(user.size);
console.log(user.has("Larwin_151"));
console.log(user.has("hello_189"));

user.delete("Prabha_178")
console.log(user)

