/* TO BE FINISHED */


#include <iostream>
#include "ComplexNumber.h"
using namespace std;

int main() {
	
	ComplexNumber* cp1 = new ComplexNumber(2, 6);
	ComplexNumber* cp2 = new ComplexNumber(7, 11);
	ComplexNumber result = *cp1 + *cp2;

	result.printComplexNumber();


	cp1 = cp2;

	cp1->printComplexNumber();

	//aad

	
}