
class GroupOfFriends:
    def __init__(self, grName):
        self.grName = grName
        self.nrPeople = 0
    #To createa group you need at least 3 people
    def createGroup(self, prs1, prs2, prs3):
        prs1.isInGroup = True
        prs2.isInGroup = True
        prs3.isInGroup = True
        prs1.groupName = self.grName
        prs2.groupName = self.grName
        prs3.groupName = self.grName
        self.nrPeople += 3
        print(prs1.name + ", "+ prs2.name + ", " + "and " + prs3.name + " created '" + self.grName + "' group.")
        self.my_list = list()
        self.my_list.append(prs1)
        self.my_list.append(prs2)
        self.my_list.append(prs3)


    def addPersonToGroup(self, prs):
        prs.isInGroup = True
        prs.groupName = self.grName
        self.nrPeople += 1
        print(prs.name + " added to '"+ self.grName + "' group.")
        self.my_list.append(prs)
    
    def removePersonFromGroup(self, prs):
        prs.isInGroup = False
        prs.groupName = None
        isInList = False
        for obj in self.my_list: 
            if obj.name is prs.name:
                isInList = True
        if isInList:
            self.nrPeople -= 1
            self.my_list.remove(prs)
            print(prs.name + " removed from '"+ self.grName + "' group.")
        else: 
            print("This person is not in the group!")
    
    def displayPeopleInGroup(self):
        print("People current in '" + self.grName + "' group:")
        for obj in self.my_list:
            print(obj.name)
    
    