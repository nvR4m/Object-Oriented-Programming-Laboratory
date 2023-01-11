#include "Group.h"
using namespace std;

Group::Group(string groupName) {
	this->groupName = groupName;
}
string Group::getGroupName() {
	return this->groupName;
}
void Group::addStudentToGroup(Student* student) {

	this->groupOfStudents.push_back(student);

}
void Group::displayStudents() {
	cout << "==" << this->getGroupName() << "==" << endl;;
	for (Student* const& i : this->groupOfStudents) {
		cout << "Name: " << i->getName() << ", grade: " << i->getGrade() << endl;
	}
	//cout << endl;
}

Group::Student::Student(string name, int grade) {
	this->name = name;
	this->grade = grade;
}

string Group::Student::getName() {
	return this->name;
}

int Group::Student::getGrade() {
	return this->grade;
}