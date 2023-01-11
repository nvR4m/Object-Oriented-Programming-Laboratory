#include <iostream>
#include "Wheel.h"
#include "Carriage.h"
using namespace std;
int main()
{
    Wheel* wh1 = new Wheel(10, true, 2.4);
    Wheel* wh2 = new Wheel(10, true, 5.3);

    Carriage* cr1 = new Carriage(20, wh1);

    cout << cr1->getSetOfWheels()->getSize() << endl;
    cr1->changeWheels(wh2);
    cout<<cr1->getSetOfWheels()->getWeareLevel();
}

