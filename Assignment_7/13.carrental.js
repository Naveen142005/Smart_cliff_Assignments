class Car {
    constructor(brand, model, pricePerDay, available) {
        this.brand = brand;
        this.model = model;
        this.pricePerDay = pricePerDay;
        this.available = available;
    }
    
    rent(days) {
        if (!this.available) {
            return "Car not available";
        }
        const totalCost = days * this.pricePerDay;
        return `Total rental cost for ${days} days is $${totalCost}.`;
    }

    returnCar() {
        this.available = true;
        return "Car returned successfully.";
    }

    getInfo() {
        return `Car: ${this.brand} ${this.model}, Price per day: $${this.pricePerDay}, Available: ${this.available}`;
    }

}

        const car = new Car("Toyota", "Camry", 50, true);
        const car2 = new Car("Honda", "Civic", 40, false);
        const car3 = new Car("Ford", "Mustang", 80, true);

        console.log(car.rent(3));
        console.log(car2.rent(2));
        console.log(car3.rent(5));
        console.log(car.getInfo());