from operator import attrgetter

class ListStudents: 
    def __init__(self):
        self.my_list = list()
    def addStudent(self, std):
        self.my_list.append(std)
    def maximumGrade(self):
        std = max(self.my_list, key=attrgetter('grade'))
        return std
    def retrunGradeEqual5(self):
        for obj in self.my_list:
            if obj.grade == 5.00:
                return obj
        print("There is no student with a grade of 5!")
        return None