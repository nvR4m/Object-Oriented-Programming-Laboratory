'''
HOMEWORK 4
IRIMIA ANDREI - CEN2.2A

4. WRITE CLASS CAR AND DRIVER, SWAP DRIVERS OF EACH CAR
'''
from Classes.Driver import Driver
from Classes.Car import Car

#Creting cars and drivers 
drv1 = Driver("Eugen", 22)
drv2 = Driver("Dani", 25)

car1 = Car(3, drv1)
car2 = Car(5, drv2)


print("The frist car driver is: " + car1.driver.name)
print("The second car driver is: " + car2.driver.name)
print("===SWAPPING===")

def swapDrivers(car1, car2):
    aux = car1.driver.name 
    car1.driver.name = car2.driver.name
    car2.driver.name = aux

swapDrivers(car1, car2)
print("The frist car driver is: " + car1.driver.name)
print("The second car driver is: " + car2.driver.name)