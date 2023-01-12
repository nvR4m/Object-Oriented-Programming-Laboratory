#include <iostream>
#include <list>
#include "Car.h"
#include "Driver.h"
using namespace std;
int main()
{
    Car* car1 = new Car("Honda", "DJ12ASR");
    Driver* drv1 = new Driver("Ginel", 12343125, car1);
    car1->setDriver(drv1);

    Car* car2 = new Car("Seat", "DJ22BFD");
    Driver* drv2 = new Driver("Dorel", 12651525, car2);
    car2->setDriver(drv2);

    Car* car3 = new Car("BMW", "DJ69BOB");
    Driver* drv3 = new Driver("Cornel", 9999, car3);
    car3->setDriver(drv3);

    list<Driver*>driverList;
    driverList.push_back(drv1);
    driverList.push_back(drv2);
    driverList.push_back(drv3);

   
    cout << "There are " << driverList.size() << " driviers in the list." << endl;
    for (Driver* const& i : driverList) {
        cout << "Name: " << i->getName() << ", Car: " << i->getCar() << ", License plate: " << i->getCar()->getLicensePlate() << endl;

    }
    driverList.remove(drv2);


    

}


