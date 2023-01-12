#pragma once
#include "Person.h"

Person::Person(string name, int age) {
	this->name = name;
	this->age = age;
}
int Person::getAge() {
	return this->age;
}