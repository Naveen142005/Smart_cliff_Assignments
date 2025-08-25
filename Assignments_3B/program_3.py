class School:
    totalStudents = 0
    MAX_CAPACITY = 500

    def enrollStudent(self):
        if School.totalStudents < School.MAX_CAPACITY:
            School.totalStudents += 1

    def getTotalStudents(self):
        return School.totalStudents


def main():
    s = School()
    for i in range(20):
        s.enrollStudent()


    print("Total Students:", s.getTotalStudents())

if __name__ == "__main__":
    main()
