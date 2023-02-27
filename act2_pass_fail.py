class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def student_detail(self):
        if self.marks >= 40:
            print(f"{self.name}: PASS")
            print(f"Score: {self.marks} marks")
        else:
            print(f"{self.name}: FAIL")
            print(f"Score: {self.marks} marks")

student1 = Student("Dorji", 50)
student1.student_detail()

student2 = Student("Dechen", 39)
student2.student_detail()

student3 = Student("Deki", 90)
student3.student_detail()


