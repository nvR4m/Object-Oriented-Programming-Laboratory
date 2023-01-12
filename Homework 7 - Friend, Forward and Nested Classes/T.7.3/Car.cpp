#include "Car.h"
Car::Car(string model, string licensePlate) {
	this->model = model;
	this->licensePlate = licensePlate;
	this->driver = nullptr;
}
string Car::getModel() {
	return this->model;
}
string Car::getLicensePlate() {
	return this->licensePlate;
}
Driver* Car::getDriver() {
	return this->driver;
}
void Car::setDriver(Driver* driver) {
	this->driver = driver;
}