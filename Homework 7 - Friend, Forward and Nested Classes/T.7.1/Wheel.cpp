#include "Wheel.h"

Wheel::Wheel(int size, bool isForCarriage, double weareLevel) {
	this->size = size;
	this->isForCarriage = isForCarriage;
	this->weareLevel = weareLevel;
}
int Wheel::getSize() {
	return this->size;
}
bool Wheel::getIsForCarriage() {
	return this->isForCarriage;
}
double Wheel::getWeareLevel() {
	return this->weareLevel;
}
void Wheel::setWeareLevel(double weareLevel) {
	this->weareLevel = weareLevel;
}
