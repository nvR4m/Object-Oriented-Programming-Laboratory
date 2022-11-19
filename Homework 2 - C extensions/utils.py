from Classes.Student import Student
from datetime import datetime
import sys
import math
from Classes.NrComplex import NrComplex
from Classes.Cat import Cat
from Classes.Car import Car
from Classes.Person import Person
def interchange(x, y):
    x = float(x)
    y = float(y)
    aux = x
    x = y 
    y = aux
    return x,y

def f(n, isRoundedTo100):
    if isRoundedTo100:
        if round(n) % 100 < 50:
            return round(n) - (round(n) % 100)
        return round(n) + 100 - (round(n) % 100)
    return round(n)

def max(s1, s2):
    if s1.grade > s2.grade:
        return s1
    elif s1.grade < s2.grade:
        return s2
    print("Student grades are the equal")

def timeToString():
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return date_time

def size(x):
    return sys.getsizeof(x)

def module(nr):
    if isinstance(nr, NrComplex):
        return math.sqrt(math.pow(nr.a,2) + math.pow(nr.b,2))
    return abs(nr)
def maximumOfThree(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    if a > b:
        if a > c:
            return a
    if b > a:
        if b > c:
            return b
    return c

def sum2(a, b):
    a = float(a)
    b = float(b)
    return a + b
    
def computeResult(a,b,c):
    if(c is '-'):
        return a-b
    elif(c is '+'):
        return a+b
    elif(c is '*'):
        return a*b
    elif(c is '/'):
        return a/b
    else: 
        return "Invalid operator"

def returnMinAge(a,b):
    if a.age < b.age:
        return a
    return b

def isSameAge(a,b):
    if type(a) is type(b):
        if a.age is b.age:
            return True
    return False        


