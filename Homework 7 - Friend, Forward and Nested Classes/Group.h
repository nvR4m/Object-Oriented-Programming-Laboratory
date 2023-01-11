#include <list>
#include <string>
#include <iostream>

using namespace std;

class Group {
private:
	class Student;
	list<Student*>groupOfStudents;
	string groupName;
public:

	class Student {
	private:
		string name;
		int grade; 
	public:
		Student(string, int);
		string getName();
		int getGrade();
	};

	Group(string);
	void addStudentToGroup(Student*);
	void displayStudents();
	string getGroupName();


};