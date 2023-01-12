#include "Driver.h"
Driver::Driver(string name, long licenseID, Car* car) {
	this->name = name;
	this->licenseID = licenseID;
	this->car = car;
}
string Driver::getName() {
	return this->name;
}
long Driver::getLicenseID() {
	return this->licenseID;
}
Car* Driver::getCar() {
	return this->car;
}