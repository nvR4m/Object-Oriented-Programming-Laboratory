'''
HOMEWORK 3
IRIMIA ANDREI - CEN2.2A

1. COMPUTE THE PAERIMETER AND AREA OF A RECTANGLE. COMPARE RECRANGLES. 
2. CREATE A LIST OF STUDENT OBJECTS AND SORT THE LIST BASED ON MULTIPLE CRITERIA.
3. SEARCH THE LIST FOR A SPECIFIC STUDENT 
4. WRITE FUNCTION THAT RETURNS STUDENT(s) WITH THE HIGHEST GRADE
5. CREATE CLASS COMPLEX NUMBER. USE IT TO COMPUTE THE SUM AND PRODUCT OF TWO COMPLEX NUMBERS
7. COUNT HOW MANY INSTANCES OF STUDENT CLASS ARE MADE

'''
from utils import compareArea, comparePerimeter, getHighestGrade, computeSumComplex, computeProdComplex
from Classes.Rectange import Rectangle
from Classes.Student import Student
from Classes.ComplexNumber import ComplexNumber

#1
print("---------------------------")
rc1 = Rectangle(5, 2)
rc2 = Rectangle(10, 4)
compareArea(rc1,rc2)
comparePerimeter(rc1,rc2)
print("---------------------------")

#2
list = []
list.append(Student("Cosmin Papa-Lapte", 19, 1, 10.00))
list.append(Student("Barbu de la Corabia", 20, 2, 5.50))
list.append(Student("Blejan Gagauta", 20, 2, 5.40))
list.append(Student("Alexandru zis-HD", 21, 3, 9.90))
list.append(Student("Ciorgan Baiatu-Mamii", 22, 4, 10.00))
list.append(Student("Serban Migos", 18, 2, 6.00))
list.append(Student("Bahoi de la Constanta", 35, 1, 2.00))

print("List of Students: ")
for obj in list: 
    print("Student: " + obj.name + ", age: " + str(obj.age) + ", academic year: " + str(obj.academic_year) + ", grade: " + str(obj.grade))

list.sort(key = lambda x: x.age)
print("List of Students sorted by age: ")
for obj in list: 
    print("Student: " + obj.name + ", age: " + str(obj.age) + ", academic year: " + str(obj.academic_year) + ", grade: " + str(obj.grade))

list.sort(key = lambda x: x.academic_year)
print("List of Students sorted by academic year: ")
for obj in list: 
    print("Student: " + obj.name + ", age: " + str(obj.age) + ", academic year: " + str(obj.academic_year) + ", grade: " + str(obj.grade))

list.sort(key = lambda x: x.grade)
print("List of Students sorted by grade: ")
for obj in list: 
    print("Student: " + obj.name + ", age: " + str(obj.age) + ", academic year: " + str(obj.academic_year) + ", grade: " + str(obj.grade))
print("---------------------------")

#3
#searching the list for student 'Cosmin Papa-Lapte'. 
for obj in list:
    if obj.name is "Cosmin Papa-Lapte":
        print(obj.name)
print("---------------------------")

#4
highest_grade_list = getHighestGrade(list)
print("Student(s) with the highest grades are: ")
for obj in highest_grade_list:
    print("Student " + obj.name + " with a grade of: " + str(obj.grade))
print("---------------------------")

#5
cn1 = ComplexNumber(2, 5)
cn2 = ComplexNumber(4, 7)
print("The first complex number is: ") 
cn1.display_complex()
print("The second complex number is: ") 
cn2.display_complex()
summed_cn = computeSumComplex(cn1, cn2)
product_cn = computeProdComplex(cn1, cn2)
print("The sum of those 2 numbers is: ")
summed_cn.display_complex()
print("The product of those 2 numbers is: ")
product_cn.display_complex()
print("---------------------------")

#7
print("There are " + str(Student.counter) + " instances of Student class")
print("---------------------------")






