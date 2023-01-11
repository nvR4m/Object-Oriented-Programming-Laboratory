/* IRIMIA ANDREI CEN2.2A */
/* 11.01.2023 */
#include <iostream>
#include "ComplexNumber.h"
using namespace std;

int main() {
	
	ComplexNumber* cp1 = new ComplexNumber(2, 6);
	ComplexNumber* cp2 = new ComplexNumber(3, 4);

	cout << "First number: ";
	cp1->printComplexNumber();
	cout << "Second number: ";
	cp2->printComplexNumber();

	double result = ~(*cp1);
	cout << "The absolute value of the first number is: " << result << endl;

	cout << "The second number raised to the power of 2 is: ";
	ComplexNumber cp3 = *cp2 ^ 2;
	cp3.printComplexNumber();

	cout << "The sum of both numbers is: ";
	cp3 = *cp1 + *cp2;
	cp3.printComplexNumber();

}