#pragma once
#include <string>
using namespace std;

class Car {
private:
	string model;
	int age;
public:
	Car(string, int);
	int getAge();
};
