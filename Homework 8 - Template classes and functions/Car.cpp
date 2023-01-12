#include "Car.h"

Car::Car(string model, int age) {
	this->model = model;
	this->age = age;
}
int Car::getAge() {
	return this->age;
}