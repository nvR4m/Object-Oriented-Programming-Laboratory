'''
HOMEWORK 2
IRIMIA ANDREI - CEN2.2A

1. WRITE A FUNCTION THAT INTERCHANGES TO VARIABLES. IT IS NOT POSSIBLE TO USE PARAMETERS AS REFERENCE IN PYTHON SO I MODIFIED THE CODE A LITTLE. 
2. WRTIE AND USE A FUNCTION 'f(n, isRoundedTo100)'. IF 'isRoundedTo100 == True' THE FUNCTION RETURNS THE CLOSEST MULTIPLE BY 100, OTHERWISE IT RETURNS THE CLOSEST INTEGER TO 'n'. 
4. WRITE A FUNCTION THAT RETURNS CURRENT DATE/TIME. 
5. WRITE A FUNCTION THAT RETURNS THE SIZE OF A PARAMETER. 
7. WRITE A FUNCTION THAT COMPUTES THE ABOSLUTE VALUE OF A COMPLEX NUMBER AND AN INTEGER VALUE. 
8. WRITE A FUNCTION THAT RETURNS THE MAXIMUM OF THREE NUMBERS. 
9. WRITE A FUNCTION THAT RETURNS THE SUM OF TWO NUMBERS. 
10. MODIFY 'interchange' FUCNTION 
11. WRITE A FUNCTION THAT TAKES TWO NUMBERS 'a' AND 'b' AND AN OPERATOR 'c' AND COMPUTES THE RESULT 
12. WRITE 3 CLASSES: 'Cat', 'Person', 'Car'. WRITE FUNCTION THAT RETURNS THE MINIM AGE. WRITE FUNCTION THAT RETURNS TURE IF OBJECTS OF THE SAME TYPE ARE THE SAME AGE OR FALSE IF DIFFERENT OBJECTS 
13. MAKE LIST OF CLASS PERSON. SORT LIST BY AGE.
14. SOLVE THE EQUATION 'ax+b=0'

'''

#1
from utils import interchange, f, max, timeToString, size, module, maximumOfThree, sum2, computeResult, returnMinAge, isSameAge
from Classes.Student import Student
from Classes.NrComplex import NrComplex
from Classes.Cat import Cat
from Classes.Car import Car
from Classes.Person import Person
import inspect

a = 1
b = 2
print("---------------------------")
print("Element a = " + str(a))
print("Element b = " + str(b))
a,b = interchange(a,b)
print("Elemets after the interchange are: a = " + str(a) + " and b = " + str(b))
print("---------------------------")

#2
n = 17.3
isRoundedTo100 = False
print("Number is n = " + str(n) + " and isRoundedTo100 is "+ str(isRoundedTo100))
print("Returned number is " + str(f(n, isRoundedTo100)))
n = 412.124
isRoundedTo100 = True
print("Number is n = " + str(n) + " and isRoundedTo100 is "+ str(isRoundedTo100))
print("Returned number is " + str(f(n, isRoundedTo100)))
print("---------------------------")

#3
student1 = Student("Gica", 18, 9.8)
student2 = Student("Marcel", 17, 7.8)
print("Student: " + student1.name + ", age: " + str(student1.age) + ", grade: " + str(student1.grade))
print("Student: " + student2.name + ", age: " + str(student2.age) + ", grade: " + str(student2.grade))
student3 = max(student1, student2)
if student3 is not None:
    print("Student with the higher grade is: " + student3.name + " with a grade of: " + str(student3.grade))
print("---------------------------")

#4
print("Current date and time is: " + timeToString())
print("---------------------------")

#5
x = 34
# x = "asdada"
# x = 1.41
# x = True
print("x = " + str(x) + ". The size of x is: " + str(size(x)))
print("---------------------------")

#7
complex1 = NrComplex(2,4)
integer = -42
print("The absolute value of " + str(complex1.a) + "+" + str(complex1.b) + "i is: " + str(module(complex1)))
print("The aboslute value of " + str(integer) + " is: " + str(module(integer)))
print("---------------------------")

#8
print("The maximum value of float(3.31), int(14) and string(\"154\") is: " + str(maximumOfThree(34.31,14,"10")))
print("---------------------------")

#9
a = 2.51
b = 1.51312
print("The sum of: "+ str(a) + " and: " + str(b) + " is: " + str(sum2(a,b)))
print("---------------------------")

#10
####

#11
a = 3
b = 5
c = '*'
print("The result of: " + str(a) + c + str(b) + " is: " + str(computeResult(a,b,c)))
print("---------------------------")

#12
cat1 = Cat("PisicaSmecheroasa", "Gigel Costel", 3)
person1 = Person("Gigel Costel", 24)
person2 = Person("Marian Regele", 24)
car1 = Car("Lada", "OT01GGC", 43)

objectMinAge = returnMinAge(cat1, person1)
print("The object with minimum age is: " + str(objectMinAge.name))
print("Are the object the same, and the same age? Response: " + str(isSameAge(person1, person2)))
print("---------------------------")

#13
list = []
list.append(person1)
list.append(person2)
list.append(Person("Cosmin Papa-Lapte", 12))
list.append(Person("Andreius Baiat-de-Plus", 19))
list.append(Person("Alexut Baiatu-Mamii", 16))
print("List order now: ")
for obj in list:
    print("Name: " + obj.name + ", age: " + str(obj.age))
print("Sorted list: ")
list.sort(key=lambda x: x.age, reverse=False)
for obj in list:
    print("Name: " + obj.name + ", age: " + str(obj.age))
print("---------------------------")

#14
a = 123.4123
b = -3
print("Equation is: " + str(a) + "x+" + str(b) +"=0")
try:
    x = -b/a
    print("Solution is: " + str(x))
except ZeroDivisionError:
    print("Equation has no soluction. 'a' parameter can't be 0")
except:
    print("Something went wrong!")




