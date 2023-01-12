#include <iostream>
#include "Person.h"
#include "Car.h"
#include "AverageAge.h"
using namespace std;

int main() {
    Person p1("Georgel", 12);
    Person p2("Marin", 43);
    Person p3("Costel", 65);
    Car c1("Toyota", 2);
    Car c2("Honda", 4);
    Car c3("BMW", 12);

    list<Person> people = { p1, p2, p3 };
    list<Car> cars = { c1, c2, c3 };

    AverageAge<Person> peopleTemplate(people);
    AverageAge<Car> carsTemplate(cars);

    cout << "Average age of people: " << peopleTemplate.average() << endl;
    cout << "Average age of cars: " << carsTemplate.average() << endl;

    return 0;
}