class Student:
    counter = 0
    def __init__(self, name, age, academic_year, grade):
        self.name = name
        self.age = age
        self.academic_year = academic_year
        self.grade = grade
        Student.counter += 1
    