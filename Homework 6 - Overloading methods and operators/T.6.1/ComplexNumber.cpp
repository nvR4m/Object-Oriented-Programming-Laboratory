#include "ComplexNumber.h"
#include <iostream>
using namespace std;

ComplexNumber::ComplexNumber(double realPart, double imagPart) {
	this->realPart = realPart;
	this->imagPart = imagPart;
}

double ComplexNumber::operator~() {
	return sqrt(pow(this->realPart, 2) + pow(this->imagPart, 2));
}

ComplexNumber ComplexNumber::operator^ (int power) {
	ComplexNumber res{ *this };
	power = 2;
	res.realPart = pow(this->realPart, power) + pow(this->imagPart, power);
	res.imagPart = power * this->realPart * this->imagPart;
	return res;
}

ComplexNumber ComplexNumber::operator+ (const ComplexNumber& cp) {
	ComplexNumber res{ *this };
	res.imagPart = this->imagPart + cp.imagPart;
	res.realPart = this->realPart + cp.realPart;
	return res;
}

void ComplexNumber::printComplexNumber() {
	cout << this->realPart << "+" << this->imagPart << "i"<<endl;
}
