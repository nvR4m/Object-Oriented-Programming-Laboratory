'''
HOMEWORK 4
IRIMIA ANDREI - CEN2.2A

2. CONSIDERING CLASSES 'Student' AND 'StudentList' WRITE A METHOD THAT RETURNS AN INSTANCE OF THE 'Student' WITH MAXIMUM GRADE
3. WRITE A METHOD THAT RETURNS THE STUDENT WITH A GRADE OF 5
'''

from Classes.Student import Student
from Classes.ListStudents import ListStudents

#2
#Creating some students 
std1 = Student("Cosminel", 1, 9.45)
std2 = Student("Alexut", 2, 5.0)
std3 = Student("Andreiut", 2, 9.90)
std4 = Student("Cristinel", 4, 10.00)
std5 = Student("Dorina", 3, 6.30)

#Creating some list objects and adding students to them
list1 = ListStudents()
list2 = ListStudents()

list1.addStudent(std1)
list1.addStudent(std2)
list1.addStudent(std3)

list2.addStudent(std4)
list2.addStudent(std5)

#Printing student with maximum grade from each list.
print("Student with the maximum grade from the first list is: " + list1.maximumGrade().name + " with a grade of: " + str(list1.maximumGrade().grade))
print("Student with the maximum grade from the second list is: " + list2.maximumGrade().name + " with a grade of: " + str(list2.maximumGrade().grade))

#3
student = list1.retrunGradeEqual5()
if student is not None:
    print(student.name + " has a grade of 5!")