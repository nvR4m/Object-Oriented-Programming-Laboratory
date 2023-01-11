#pragma once
#include <math.h>
class ComplexNumber{
private: 
	double realPart;
	double imagPart;
public:

	ComplexNumber(double, double);

	/* function used to print the imaginary number */
	void printComplexNumber();

	/* overload operator ~ to return absolute value of imaginary part */
	double operator~();

	/* overload operator ^ to return the power of 2 of the imaginary part */
	/* a = a^2 + b^2 */
	/* b = 2ab */
    /* function needs to be modified for other powers. There is no general formula for powering non-trigonometric complex numbers */
	ComplexNumber operator^(int);

	/* overload operator + to add two complex numbers */
	ComplexNumber operator+(const ComplexNumber&);
};
