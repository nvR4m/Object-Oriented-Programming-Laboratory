#pragma once
#include <iostream>
using namespace std;
class Carriage {
private:
	double km;
	Wheel* setOfWheels;
	int neededWheelSize = 10;
public:
	Carriage(double, Wheel*);
	void goSomewhere(double);
	void changeWheels(Wheel*);
	double getKm();
	Wheel* getSetOfWheels();
	
};
