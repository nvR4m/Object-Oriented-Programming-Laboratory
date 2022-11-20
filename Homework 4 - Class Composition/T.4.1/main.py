'''
HOMEWORK 4
IRIMIA ANDREI - CEN2.2A

1. DEFINE CLASS 'Person' and 'GroupOfFriends'. IMPLEMENT METHODS LIKE CREATE A GROUP, ADD/REMOVE/UPDATE A PERSON, DISPLAY THE PERSONS IN THE GROUP.
'''
from Classes.GroupOfFriends import GroupOfFriends
from Classes.Person import Person

#Creating some people
prs1 = Person("Gica", 20, "Male")
prs2 = Person("Costel", 21, "Male")
prs3 = Person("Marin", 19, "Male")
prs4 = Person("Gigela", 15, "Female")
prs5 = Person("Florentina", 17, "Female")
prs6 = Person("Gigi", 14, "Male")

#Creating the groups.
gr1 = GroupOfFriends("Gagicarii")
gr1.createGroup(prs1, prs2, prs3)

gr2 = GroupOfFriends("Smecherii")
gr2.createGroup(prs4, prs5, prs6)

#Removing person3 from first group and adding it to the second.
gr1.removePersonFromGroup(prs3)
gr2.addPersonToGroup(prs3)

#Displayng groups.
gr1.displayPeopleInGroup()
gr2.displayPeopleInGroup()