class Student:
    def __init__(self, student_id=0, name= "Unknown", age = 0, grade = "Unknown"):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

def main():
    s1 = Student()
    print(s1.student_id , s1.name , s1.age , s1.grade)

    s2 = Student(101, "Alice", 15, "A")
    print(s2.student_id, s2.name, s2.age, s2.grade)

if __name__ == "__main__":
    main()
