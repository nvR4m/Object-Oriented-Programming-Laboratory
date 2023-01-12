#pragma once
#include <string>
using namespace std;
class Car;
class Driver {
private:
	string name;
	long licenseID;
	Car* car;
public:
	Driver(string, long, Car*);
	string getName();
	long getLicenseID();
	Car* getCar();
};