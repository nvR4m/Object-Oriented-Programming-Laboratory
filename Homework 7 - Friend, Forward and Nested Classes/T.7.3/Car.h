#pragma once
#include <string>
using namespace std;
class Driver;
class Car {
protected:
	string model;
	string licensePlate;
	Driver* driver;
public:
	Car(string, string);
	string getModel();
	string getLicensePlate();
	Driver* getDriver();
	void setDriver(Driver*);
};