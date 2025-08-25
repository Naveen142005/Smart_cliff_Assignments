from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class ElectricVehicle(ABC):
    @abstractmethod

    def charge(self):
        pass

class GasVehicle(ABC):
    @abstractmethod

    def refuel(self):
        pass

class ElectricCar(Vehicle, ElectricVehicle):

    def start(self):
        print("Electric car started")
    def stop(self):
        print("Electric car stopped")
    def charge(self):
        print("Charging electric car")

class GasMotorcycle(Vehicle, GasVehicle):
    def start(self):
        print("Gas vehicle started")
    def stop(self): print("Gas vehicle stopped")
    def refuel(self): print("Refuel the gas vehile")

def main():
    #For electirc car
    e = ElectricCar()
    e.start();
    e.charge();
    e.stop()

    #for Gas vehicle
    g = GasMotorcycle()
    g.start();
    g.refuel();
    g.stop()

if __name__=="__main__":
    main()
