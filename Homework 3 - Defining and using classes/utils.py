from Classes.Rectange import Rectangle 
from Classes.ComplexNumber import ComplexNumber
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

def computeSumComplex(a,b):
    sumr = a.real_part + b.real_part
    sumi = a.imag_part + b.imag_part
    summed_number = ComplexNumber(sumr, sumi)
    return summed_number

def computeProdComplex(a,b):
    #compute the real part
    r_part = a.real_part * b.real_part - a.imag_part * b.imag_part
    #compute the imaginary part
    i_part = a.real_part * b.imag_part + a.imag_part * b.real_part
    product_number = ComplexNumber(r_part, i_part)
    return product_number


