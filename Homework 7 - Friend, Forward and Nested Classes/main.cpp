#include<iostream>
#include "Group.h"
using namespace std;


int main() {

	Group::Student* s1 = new Group::Student("Gica", 3);
	Group::Student* s2 = new Group::Student("Georgel", 6);
	Group::Student* s3 = new Group::Student("Marian", 10);
	Group::Student* s4 = new Group::Student("Ionel", 2);
	Group::Student* s5 = new Group::Student("Marcel", 9);
	Group gr1("Smecherii");
	Group gr2("Bisnitarii");

	gr1.addStudentToGroup(s1);
	gr1.addStudentToGroup(s2);
	gr1.addStudentToGroup(s3);

	gr2.addStudentToGroup(s4);
	gr2.addStudentToGroup(s5);


	gr1.displayStudents();
	gr2.displayStudents();
	
}