from Classes.Rectange import Rectangle 
from operator import attrgetter

def compareArea(a,b):
    if a.computeArea() > b.computeArea():
        print("Area of the first rectangle is bigger!")
    else:
        print("Area of the second rectangle is bigger!")

def comparePerimeter(a,b):
    if a.computePerimeter() > b.computePerimeter():
        print("Perimeter of the first rectangle is bigger!")
    else:
        print("Perimeter of the second rectangle is bigger!")

def getHighestGrade(list):
    new_list = []
    student = max(list, key=attrgetter('grade'))
    for obj in list: 
        if student.grade is obj.grade:
            new_list.append(obj)
    return new_list


