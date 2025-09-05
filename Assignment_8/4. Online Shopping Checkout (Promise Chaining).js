function loginUser(email, password) {
    return new Promise((resolve, reject) => {
        console.log("Logging in...");
        setTimeout(() => {
            resolve("User logged in");
        }, 2000);
    });
}

const payment = () => {
    return new Promise((resolve, reject) => {
        console.log("Payment processing...");
        setTimeout(() => {
            resolve("Payment successful");
        }, 2100);
    });
}

       
loginUser("user@example.com", "password123")
    .then(user => {
        console.log(user);
        return payment();
    })
    .then(status_ => {
        console.log(status_);
    })
    .catch(error => {
        console.error("Login failed:", error);
    });