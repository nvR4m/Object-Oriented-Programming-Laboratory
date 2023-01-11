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

	/* overload operator ~ to return absolute value of complex number */
	double operator~();

	/* overload operator ^ to return the power of 2 of the complex number */
	/* a = a^2 + b^2 */
	/* b = 2ab */
    /* function needs to be modified for other powers. There is no general formula for powering non-trigonometric complex numbers */
	ComplexNumber operator^(int);

	/* overload operator + to add two complex numbers */
	ComplexNumber operator+(const ComplexNumber&);

	/* overload operator < to compare the abs. values of the complex numbers */
	bool operator<(ComplexNumber);
};
