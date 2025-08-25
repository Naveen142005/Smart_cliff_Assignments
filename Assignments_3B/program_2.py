class Employee:
    def getInfo(self, salary, hours):
        self.salary = salary
        self.hours = hours

    def AddSal(self):
        if self.salary < 500:
            self.salary += 10

    def AddWork(self):
        if self.hours > 6:
            self.salary += 5


def main():
    salary = int(input("Enter salary: "))
    hours = int(input("Enter work hours per day: "))

    emp = Employee()
    emp.getInfo(salary, hours)
    emp.AddSal()
    emp.AddWork()

    print("Final Salary:", emp.salary)


if __name__ == "__main__":
    main()
