from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, eid , name):
        self.eid = eid
        self.name = name

    def displayInfo(self):
        print(self.eid ,self.name)

    @abstractmethod
    def calculateSalary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, eid , name, salary ):
        super().__init__(eid, name)
        self.salary = salary
    def calculateSalary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, eid,name , rate , hours):
        super().__init__(eid,name)
        self.rate = rate
        self.hours = hours
    def calculateSalary(self):
        return self.rate * self.hours

class ContractEmployee(Employee):
    def __init__(self, eid , name , rate , months):
        super().__init__(eid , name)
        self.rate = rate
        self.months = months
    def calculateSalary(self):
        return self.rate * self.months

def main():
    fte = FullTimeEmployee(1 , "Naveen" ,50000)
    fte.displayInfo()
    print("Salary:", fte.calculateSalary())

    pte = PartTimeEmployee(2,"Thagalzhi", 20 ,100)
    pte.displayInfo()
    print("Salary:" , pte.calculateSalary())

    ce = ContractEmployee(3 , "Yalzhini",2000,6)
    ce.displayInfo()
    print("Salary:" ,ce.calculateSalary())

if __name__ == "__main__":
    main()
