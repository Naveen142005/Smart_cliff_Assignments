class Vehicle:
    def __init__(self, brand="", year=0):
        self.brand = brand
        self.year = year

    def displayInfo(self):
        print("Brand:", self.brand)
        print("Year:", self.year)


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def displayCarInfo(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


def main():
    brand = input("Enter brand ")
    year = int(input("Enter  year: "))
    model = input("Enter model: ")

    my_car = Car(brand, year, model)
    print("\nVehicle Info:")
    my_car.displayInfo()

    print("\nCar Info:")
    my_car.displayCarInfo()


if __name__ == "__main__":
    main()
