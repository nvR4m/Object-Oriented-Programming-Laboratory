#include "Wheel.h"
#include "Carriage.h"

Carriage::Carriage(double km, Wheel* setOfWheels){
	this->km = km;
	this->setOfWheels = setOfWheels;
}

Wheel* Carriage::getSetOfWheels() {
	return this->setOfWheels;
}

double Carriage::getKm() {
	return this->km;
}

void Carriage::goSomewhere(double distanceTraveled) {
	if (this->getSetOfWheels()->getWeareLevel() >= 100) {
		cout << "Wheels are too damaged for the trip!" << endl;
	}
	else {
		this->km += distanceTraveled;
		this->getSetOfWheels()->setWeareLevel(this->getSetOfWheels()->getWeareLevel() + distanceTraveled / 100);
	}
}
void Carriage::changeWheels(Wheel* newSetOfWheels) {

	if (this->neededWheelSize == newSetOfWheels->getSize() && newSetOfWheels->getIsForCarriage() == true) {
		this->setOfWheels = newSetOfWheels;
	}
	else {
		cout << "Can't change wheels. Tire size needs to be 10 and for CARRIAGE!";
	}

}

