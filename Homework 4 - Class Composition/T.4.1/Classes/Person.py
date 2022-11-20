class Person: 
    def __init__(self, name, age, gender, isInGroup = False, groupName = None):
        self.name = name
        self.age = age
        self.gender = gender
        if self.age <= 18:
            self.isAdult = False
        else:
            self.isAdult = True
